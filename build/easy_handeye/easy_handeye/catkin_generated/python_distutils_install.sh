#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/elephant/catkin_ws/src/easy_handeye/easy_handeye"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/elephant/catkin_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/elephant/catkin_ws/install/lib/python2.7/dist-packages:/home/elephant/catkin_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/elephant/catkin_ws/build" \
    "/usr/bin/python2" \
    "/home/elephant/catkin_ws/src/easy_handeye/easy_handeye/setup.py" \
    egg_info --egg-base /home/elephant/catkin_ws/build/easy_handeye/easy_handeye \
    build --build-base "/home/elephant/catkin_ws/build/easy_handeye/easy_handeye" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/elephant/catkin_ws/install" --install-scripts="/home/elephant/catkin_ws/install/bin"
