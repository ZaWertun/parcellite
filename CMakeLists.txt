project(parcellite)
cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

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

add_definitions(${GTK2_CFLAGS_OTHER})

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -pedantic -Wall -Wextra")
target_compile_definitions(parcellite PRIVATE GETTEXT_PACKAGE="parcellite" PARCELLITELOCALEDIR="/usr/parcellite/locale")
target_link_libraries(parcellite ${X11_LIBRARIES} ${GTK2_LIBRARIES})
