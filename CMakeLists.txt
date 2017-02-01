cmake_minimum_required(VERSION 3.1 FATAL_ERROR)

project(parcellite)

find_package(PkgConfig REQUIRED)
find_package(X11 REQUIRED)
pkg_check_modules(GTK2 REQUIRED gtk+-2.0)

include_directories(${X11_INCLUDE_DIR} ${GTK2_INCLUDE_DIRS})
link_directories(${GTK2_LIBRARY_DIRS})

add_executable(parcellite src/attr_list.c
        src/daemon.c
        src/eggaccelerators.c
        src/history.c
        src/keybinder.c
        src/main.c
        src/preferences.c
        src/utils.c)

include(FindGettext OPTIONAL)
add_subdirectory(po)

add_definitions(${GTK2_CFLAGS_OTHER})

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wall -Wextra -Wno-unused-parameter")
target_link_libraries(parcellite ${X11_LIBRARIES} ${GTK2_LIBRARIES})

# Install binary:
install(TARGETS parcellite DESTINATION ${CMAKE_INSTALL_PREFIX}/bin)

# Install man page:
add_custom_target(man ALL)
add_custom_command(
  TARGET man
  COMMAND gzip ARGS --to-stdout ${CMAKE_CURRENT_SOURCE_DIR}/man/parcellite.1 > ${CMAKE_CURRENT_BINARY_DIR}/parcellite.1.gz
  OUTPUTS ${CMAKE_CURRENT_BINARY_DIR}/parcellite.1.gz
)
add_custom_command(TARGET man DEPENDS ${CMAKE_CURRENT_BINARY_DIR}/parcellite.1.gz)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/parcellite.1.gz DESTINATION ${CMAKE_INSTALL_PREFIX}/share/man/man1)

# Install icons:
install(FILES icons/parcellite.svg DESTINATION ${CMAKE_INSTALL_PREFIX}/share/icons/hicolor/scalable/apps)
file (GLOB ICONS "icons/*/parcellite.png")
foreach(file ${ICONS})
    get_filename_component(dir ${file} DIRECTORY)
    get_filename_component(dir ${dir} NAME)

    install(FILES ${file} DESTINATION ${CMAKE_INSTALL_PREFIX}/share/icons/hicolor/${dir}/apps)
endforeach()

# Install desktop files:
install(FILES data/parcellite.desktop DESTINATION ${CMAKE_INSTALL_PREFIX}/share/applications)
