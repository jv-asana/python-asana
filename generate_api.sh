DEFAULT_ASANA_OAS="https://raw.githubusercontent.com/Asana/developer-docs/master/defs/asana_oas.yaml"
ASANA_OAS=${CUSTOM_ASANA_OAS:-$DEFAULT_ASANA_OAS}
TEMPLATE_DIR="openapi_templates"
CURRENT_DIR=$(pwd)
ASANA_APIS_DIR=$CURRENT_DIR/asana/resources/gen
ASANA_DOCS_DIR=$CURRENT_DIR/samples

# utility function for printing error
echoerr() { echo "$@" 1>&2; }

# clean generation data
clean () {
    rm -rf $CURRENT_DIR
}

# remove Api suffix from api's class name
# use GNU sed version, for BSD/MacOS version use sed "s/pattern/replace" input > output instead -i option
remove_classname_suffix() { sed -i 's/\(class .*\)Api\(.*\)/\1\2/' $1; }

# process apis files :
# rename files and move it to asana/apis/ folder
post_process_apis() {
    # move apis files to directory asana/apis/ and remove all unused files
    mkdir $CURRENT_DIR/tmp_apis && cp $CURRENT_DIR/python-client/asana/apis/tags/* $CURRENT_DIR/tmp_apis && rm -rf $CURRENT_DIR/python-client/asana/* && \
    mkdir $CURRENT_DIR/python-client/asana/apis/ && cp $CURRENT_DIR/tmp_apis/* $CURRENT_DIR/python-client/asana/apis/ && rm -rf $CURRENT_DIR/tmp_apis
    [ $? -ne 0 ] && { echoerr "Could move apis files to needed file structure"; return 1; }

    # remove sufix _api from files
    cd "$CURRENT_DIR/python-client/asana/apis/" || return 1
    for file in *api*; do
        #trying to remove api's class name suffix
        remove_classname_suffix $file || return 1
        mv -- "$file" "${file%%_api.py}.py" || return 1
    done
    cd "$CURRENT_DIR" || return 1

    # Modify __init__.py
    echo -e "from . import *\n" > $CURRENT_DIR/python-client/asana/apis/__init__.py || return 1
    cp $CURRENT_DIR/python-client/asana/apis/* $ASANA_APIS_DIR || { echoerr "Could not copy generated files to $ASANA_APIS_DIR"; return 1; }
}

# Process docs:
# Rename docs files and move it to samples folder
post_process_docs() {
    mkdir $CURRENT_DIR/samples || return 1
    cp $CURRENT_DIR/python-client/docs/apis/tags/* $CURRENT_DIR/samples/ || return 1
    cd $CURRENT_DIR/samples || return 1
    for file in *Api.md; do
        ### lowercase docs files and remove suffix
        ### TODO :: trying to use native bash opportunities instead call tr each time
        new_file_name=$(echo "${file%%Api.md}_sample.yaml" | tr '[:upper:]' '[:lower:]')
        mv -- "$file" "$new_file_name" || return 1;
    done
    cd $CURRENT_DIR || return 1;

    cp $CURRENT_DIR/samples/* $ASANA_DOCS_DIR || { echoerr "Could not copy generated docs to $ASANA_DOCS_DIR"; return 1; }
}

post_process() {
    post_process_apis || { echoerr "Could not post process apis"; return 1; }
    post_process_docs || { echoerr "Could not post process docs"; return 1; }
}

main() {
    exit_code=0

    # generate apis
    post_process

    # clean generation folder
    clean

    exit $exit_code 
}

main