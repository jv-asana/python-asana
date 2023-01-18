DEFAULT_ASANA_OAS="https://raw.githubusercontent.com/Asana/developer-docs/master/defs/asana_oas.yaml"
ASANA_OAS=${CUSTOM_ASANA_OAS:-$DEFAULT_ASANA_OAS}
OUT_DIR="openapi_generated_files"
TEMPLATE_DIR="openapi_templates"
CURRENT_DIR=$(pwd)
OPENAPI_GENERATOR_CLI_URL="https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/6.2.1/openapi-generator-cli-6.2.1.jar"
ASANA_APIS_DIR=$CURRENT_DIR/asana/resources/gen
ASANA_DOCS_DIR=$CURRENT_DIR/samples

# utility function for printing error
echoerr() { echo "$@" 1>&2; }

# get open api generator jar
get_openapi_generator_cli() {
    if [ -z $OPENAPI_GENERATOR_CLI ]; then
        WGET=$(which wget)
        [ $? -ne 0 ] && { echoerr "wget tool was not found in system"; exit 1; }

        # trying to download openapi-generator
        OPENAPI_GENERATOR_CLI="$CURRENT_DIR/openapi-generator-cli.jar"
        $WGET "$OPENAPI_GENERATOR_CLI_URL" -O $OPENAPI_GENERATOR_CLI
        [ $? -ne 0 ] && { echoerr 'Could not download openapi-generator by "OPENAPI_GENERATOR_CLI_URL"'; exit 1; }
    fi
}

# check and install openjdk
check_java() {
    # TODO :: check if openjdk is present in system and install it otherwise
    :
}

# create working dir for store generated code
create_out_dir() {
    if [ -d $OUT_DIR ]; then
        rm -rf $OUT_DIR || { echoerr "Could not remove $OUT_DIR"; exit 1; }
    fi
    mkdir $OUT_DIR || { echoerr "Could not create $OUT_DIR"; exit 1; }
}

# prepare generation
prepare_generation() {
    check_java
    get_openapi_generator_cli
    create_out_dir
}

# clean generation data
clean () {
    rm -rf $OUT_DIR
    rm $OPENAPI_GENERATOR_CLI
}

# generate apis
generate() {
    java -jar $OPENAPI_GENERATOR_CLI generate -i $ASANA_OAS -g python -o $OUT_DIR -t $TEMPLATE_DIR \
             --global-property apis,apiDocs=true,apiTests=false -p packageName=asana
}

# remove Api suffix from api's class name
# use GNU sed version, for BSD/MacOS version use sed "s/pattern/replace" input > output instead -i option
remove_classname_suffix() { sed -i 's/\(class .*\)Api\(.*\)/\1\2/' $1; }

# process apis files :
# rename files and move it to asana/apis/ folder
post_process_apis() {
    # move apis files to directory asana/apis/ and remove all unused files
    mkdir $OUT_DIR/tmp_apis && cp $OUT_DIR/asana/apis/tags/* $OUT_DIR/tmp_apis && rm -rf $OUT_DIR/asana/* && \
    mkdir $OUT_DIR/asana/apis/ && cp $OUT_DIR/tmp_apis/* $OUT_DIR/asana/apis/ && rm -rf $OUT_DIR/tmp_apis
    [ $? -ne 0 ] && { echoerr "Could move apis files to needed file structure"; return 1; }

    # remove sufix _api from files
    cd "$OUT_DIR/asana/apis/" || return 1
    for file in *api*; do
        #trying to remove api's class name suffix
        remove_classname_suffix $file || return 1
        mv -- "$file" "${file%%_api.py}.py" || return 1
    done
    cd "$CURRENT_DIR" || return 1

    # Modify __init__.py
    echo -e "from . import *\n" > $OUT_DIR/asana/apis/__init__.py || return 1
    cp $OUT_DIR/asana/apis/* $ASANA_APIS_DIR || { echoerr "Could not copy generated files to $ASANA_APIS_DIR"; return 1; }
}

# Process docs:
# Rename docs files and move it to samples folder
post_process_docs() {
    mkdir $OUT_DIR/samples || return 1
    cp $OUT_DIR/docs/apis/tags/* $OUT_DIR/samples/ || return 1
    cd $OUT_DIR/samples || return 1
    for file in *Api.md; do
        ### lowercase docs files and remove suffix
        ### TODO :: trying to use native bash opportunities instead call tr each time
        new_file_name=$(echo "${file%%Api.md}_sample.yaml" | tr '[:upper:]' '[:lower:]')
        mv -- "$file" "$new_file_name" || return 1;
    done
    cd $CURRENT_DIR || return 1;

    cp $OUT_DIR/samples/* $ASANA_DOCS_DIR || { echoerr "Could not copy generated docs to $ASANA_DOCS_DIR"; return 1; }
}

post_process() {
    post_process_apis || { echoerr "Could not post process apis"; return 1; }
    post_process_docs || { echoerr "Could not post process docs"; return 1; }
}

main() {
    exit_code=0

    # prepare generation
    prepare_generation

    # generate apis
    generate

    # process apis if generation was success
    return_value=$?
    [ $return_value -eq 0 ] && { post_process || exit_code=$?; } || \
                            { echoerr "Generation failed"; exit_code=$return_value; }

    # clean generation folder
    clean

    exit $exit_code 
}

main