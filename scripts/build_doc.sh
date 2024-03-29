#! /bin/bash

# This script is meant to be run from the project's root directory.

build_doc() {

    # Changes to the documentation folder.
    cd ./docs/sphinx

    # Removes everything from the build folder.
    make clean

    # Creates the HTML files.
    make html

    # Changes back to the project's root folder.
    cd ..
    cd ..

}

build_doc