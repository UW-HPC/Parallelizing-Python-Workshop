getNode() {
  if [ "$2" == "" ]; then
    echo "Usage:  getNode <node number> <day>"
  else
    srun -p stf -A stf-workshop --reservation="stf-workshop_Oct$2" -w "n$1" -n 14 --mem=60G --pty /bin/bash -l
  fi
}

getGPUNode() {
  if [ "$2" == "" ]; then
    echo "Usage:  getGPUNode <node number> <day>"
  else
    srun -p stf-gpu -A stf-workshop --reservation="stf-workshop_Oct$2_gpu" -w "n$1" -n 14 --mem=60G --pty /bin/bash -l
  fi
}

echo "Welcome to Parallelizing Python!"
echo "The following commands have been added to your environment: getNode, getGPUNode"
