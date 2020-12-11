source /reg/g/psdm/sw/conda2/manage/bin/psconda.sh
conda deactivate
conda deactivate
conda activate ps-3.0.16
procmgr stopall hsd.cnf
procmgr start hsd.cnf
