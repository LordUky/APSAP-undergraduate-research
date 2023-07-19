if [ -d "build" ] 
then
    rm -r build/*
else
    mkdir build
fi

python3 -m compileall .

for x in `find -name "*.cpython-310.pyc" -type f`
do
    newdir=`dirname $(dirname "build/$x")`
    dest=`dirname $(dirname "build/$x")`/$(basename ${x/cpython-310\.})
    mkdir -p $newdir
    cp $x $dest
done



# mv build/__pycache__/main.cpython-310.pyc build/


