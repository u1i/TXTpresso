export PYTHONPATH=$PYTHONPATH:$(pwd)
echo "in another window do this: dig @localhost -p 53 +short txt time.txtpresso"
python examples/time-example.py

