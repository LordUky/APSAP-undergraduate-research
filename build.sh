if [ -d "build" ] 
then
    rm -r build/*
else
    mkdir build
fi

python3 -m compileall .

for x in `find -name "__pycache__" -type d`
do
    mkdir -p build/$x
    cp $x/* build/$x/
    cp $x/../__init__.py build/$x/../
done

mv build/__pycache__/main.cpython-310.pyc build/

