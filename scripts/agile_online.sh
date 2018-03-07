cd agile-de
python3 manage.py build
cd ..
rm -r docs/agile-de/*
cp -r agile-de/_build/assets docs/agile-de
cp -r agile-de/_build/theme docs/agile-de

cd agile-en
python3 manage.py build
cd ..
rm -r docs/agile-en/*
cp -r agile-en/_build/assets docs/agile-en
cp -r agile-en/_build/theme docs/agile-en
