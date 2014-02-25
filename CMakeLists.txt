# CMake script for building debian packages:
#
# Run the following commands:
#   - cd /path/to/src
#   - mkdir build && build
#   - cmake -DCPACK_GENERATOR=DEB ..
#   - make package
#
# To upload a PPA package, adapt DPUT_HOST to point to your ppa then run
# make dput
#
cmake_minimum_required( VERSION 2.8 )

# ##############################################################

set(PROJECT_NAME pyqode.designer)
project(pyqode.designer)
set(VERSION_MAJOR 1)
set(VERSION_MINOR 1)
set(VERSION_PATCH 0)
set(VERSION ${VERSION_MAJOR}.${VERSION_MINOR}.${VERSION_PATCH})

# Make the scripts available in the 'cmake' directory available for the
# 'include()' command, 'find_package()' command.

set( CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} ${CMAKE_CURRENT_LIST_DIR}/cmake )

# ##############################################################

set(DEPENDS "python, python-pyqode.core, qt4-designer, python-qt4-dev")
find_package(PythonInterp 2.7)
set(CPACK_TARGET_INTERPRETER_VERSION "python")
set(PIP "pip")

configure_file(
  "${PROJECT_SOURCE_DIR}/share/pyqode_designer.desktop.in"
  "${PROJECT_BINARY_DIR}/pyqode_designer.desktop"
  )
execute_process(COMMAND chmod 0644 ${PROJECT_BINARY_DIR}/pyqode_designer.desktop)

# ##############################################################

configure_file(
      "${CMAKE_SOURCE_DIR}/pyqode/designer.py"
      "${PROJECT_BINARY_DIR}/pyqode-designer"
      )

install(PROGRAMS "${PROJECT_BINARY_DIR}/pyqode-designer" DESTINATION bin)
install(FILES "${PROJECT_BINARY_DIR}/pyqode_designer.desktop"
        DESTINATION share/applications )

# ##############################################################

if(CMAKE_CPACK_COMMAND AND UNIX)
    set(DPUT_HOST "ppa:pyqode/unstable" CACHE STRING "PPA repository to upload the debian sources")

    # Packing information
    set(CPACK_PACKAGE_NAME ${CPACK_TARGET_INTERPRETER_VERSION}-${PROJECT_NAME})

    # trick to put the copyright to /usr/share/doc/<package>/
    configure_file(
      "${PROJECT_SOURCE_DIR}/LICENSE.txt"
      "${PROJECT_BINARY_DIR}/copyright"
      )
    INSTALL(FILES "${PROJECT_BINARY_DIR}/copyright"
            DESTINATION share/doc/${CPACK_PACKAGE_NAME}/)

    INSTALL(FILES "${PROJECT_BINARY_DIR}/copyright"
        DESTINATION share/doc/${CPACK_PACKAGE_NAME}/)

    set(CPACK_PACKAGE_CONTACT "Colin Duquesnoy <colin.duquesnoy@gmail.com>" CACHE STRING "Package maintainer and PGP signer.")
    set(CPACK_PACKAGE_VENDOR "https://github.com/pyQode/pyqode.designer")
    set(CPACK_PACKAGE_DISPLAY_NAME "pyqode.designer ${VERSION}")
    set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "Starts Qt Designer with pyQode plugins")
    set(CPACK_PACKAGE_VERSION "${VERSION}")
    set(CPACK_PACKAGE_VERSION_MAJOR ${VERSION_MAJOR})
    set(CPACK_PACKAGE_VERSION_MINOR ${VERSION_MINOR})
    set(CPACK_PACKAGE_VERSION_PATCH ${VERSION_PATCH})
    set(CPACK_DEBIAN_CHANGELOG
        "  * See the homepage for a full change log:\n    https://github.com/ColinDuquesnoy/pyqode.designer\n")
    set(DEB_LONG_DESCRIPTION
        " The pyqode plugins will appear in the toolbox under the 'pyqode' section\n"
        " .\n"
        " Only python 2 plugins are detected, i.e. you have to install the \n"
        " python 2 packages of pyqode to see them in the designer.\n")
    string(REPLACE ";" "" DEB_LONG_DESCRIPTION ${DEB_LONG_DESCRIPTION})
    set(CPACK_DEBIAN_PACKAGE_DESCRIPTION
        "${CPACK_PACKAGE_DESCRIPTION_SUMMARY}\n${DEB_LONG_DESCRIPTION}")
    set(CPACK_RESOURCE_FILE_LICENSE ${CMAKE_CURRENT_SOURCE_DIR}/LICENSE.txt)

    # base
    set(CPACK_DEBIAN_BUILD_DEPENDS_UBUNTU debhelper cmake ${CPACK_TARGET_INTERPRETER_VERSION})

    # get architecture
    set(CPACK_DEBIAN_PACKAGE_ARCHITECTURE "all")

    # debian
    set(CPACK_DEBIAN_PACKAGE_PRIORITY optional)
    set(CPACK_DEBIAN_PACKAGE_SECTION python)
    set(CPACK_DEBIAN_PACKAGE_DEPENDS ${DEPENDS})
    set(CPACK_DEBIAN_PACKAGE_SOURCE_COPY "${PYTHON_EXECUTABLE} /tools/copydebfiles.py")
    set(CPACK_DEBIAN_PACKAGE_REMOVE_SOURCE_FILES )
    execute_process(COMMAND lsb_release -is
        OUTPUT_VARIABLE _lsb_distribution OUTPUT_STRIP_TRAILING_WHITESPACE
        RESULT_VARIABLE _lsb_release_failed)
    if(${_lsb_distribution})
        set(CPACK_DEBIAN_DISTRIBUTION_NAME ${_lsb_distribution} CACHE STRING "Name of the distribution")
    else()
        # lsb_release fail when building the package in a ppa, as ubuntu is always the target release
        # on launchpad, we can safely set the distribution name to ubuntu
        set(CPACK_DEBIAN_DISTRIBUTION_NAME "ubuntu")
    endif()
    string(TOLOWER ${CPACK_DEBIAN_DISTRIBUTION_NAME} CPACK_DEBIAN_DISTRIBUTION_NAME)
    if( ${CPACK_DEBIAN_DISTRIBUTION_NAME} STREQUAL "ubuntu" )
        set(CPACK_DEBIAN_DISTRIBUTION_RELEASES precise quantal raring saucy CACHE STRING "Release code-names of the distrubiton release")
    endif()
    # The debian generator does not seem to use a correct name for the debian packages
    set(CPACK_PACKAGE_FILE_NAME "${CPACK_PACKAGE_NAME}_${VERSION_MAJOR}.${VERSION_MINOR}.${VERSION_PATCH}_${CPACK_DEBIAN_PACKAGE_ARCHITECTURE}")

    include(CPack)
    include(DebSourcePPA)
endif()