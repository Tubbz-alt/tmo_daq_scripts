#source /cds/group/psdm/sw/conda2/manage/bin/psconda.sh
source /cds/sw/ds/ana/conda2/manage/bin/psconda.sh
conda activate ps-4.1.0
#RELDIR="/cds/home/opr/tmoopr/git/lcls2-112320"
RELDIR="/cds/home/opr/tmoopr/git/lcls2_120320"
export PATH=$RELDIR/install/bin:${PATH}
pyver=$(python -c "import sys; print(str(sys.version_info.major)+'.'+str(sys.version_info.minor))")
export PYTHONPATH=$RELDIR/install/lib/python$pyver/site-packages
# for procmgr
export TESTRELDIR=$RELDIR/install
