if (NOT GETTEXT_FOUND)
    return()
endif()

target_compile_definitions(parcellite PUBLIC
    ENABLE_NLS
    GETTEXT_PACKAGE="parcellite"
    PARCELLITELOCALEDIR="${CMAKE_INSTALL_PREFIX}/share/locale"
)

set(src ${CMAKE_SOURCE_DIR}/src)
set(src_list
    ${src}/attr_list.c
    ${src}/daemon.c
    ${src}/eggaccelerators.c
    ${src}/history.c
    ${src}/keybinder.c
    ${src}/main.c
    ${src}/preferences.c
    ${src}/utils.c
)

execute_process(COMMAND ${CMAKE_COMMAND} -E copy_directory ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_BINARY_DIR}/)

set(pot_file ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}.pot)
add_custom_command(OUTPUT ${pot_file}
    COMMAND ${CMAKE_COMMAND} -E copy_directory ${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_BINARY_DIR}/
    COMMAND chmod a+w ${CMAKE_CURRENT_BINARY_DIR}/*.po
    COMMAND xgettext --keyword=_ --keyword=N_ -o ${pot_file} ${src_list}
    DEPENDS ${src_list}
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    COMMENT "Extract translatable messages to ${pot_file}"
)

gettext_process_pot_file(${pot_file} ALL
    INSTALL_DESTINATION "${CMAKE_INSTALL_PREFIX}/share/locale/"
    LANGUAGES
        cs
        da
        de
        es
        fr
        hu
        it
        ja
        nb
        pl
        pl_PL
        pt_BR
        ro
        ru
        sv
        tr
        zh_CN
        zh_TW
)
