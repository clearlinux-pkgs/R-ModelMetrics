#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ModelMetrics
Version  : 1.2.2
Release  : 25
URL      : https://cran.r-project.org/src/contrib/ModelMetrics_1.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ModelMetrics_1.2.2.tar.gz
Summary  : Rapid Calculation of Model Metrics
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-ModelMetrics-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-data.table
BuildRequires : R-Rcpp
BuildRequires : R-data.table
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
## ModelMetrics: Rapid Calculation of Model Metrics
[![Build Status](https://travis-ci.org/JackStat/ModelMetrics.svg?branch=master)](https://travis-ci.org/JackStat/ModelMetrics)
[![Build status](https://ci.appveyor.com/api/projects/status/evm55ctrlwp6fjs3/branch/master?svg=true)](https://ci.appveyor.com/project/JackStat/modelmetrics/branch/master)
[![Coverage Status](https://coveralls.io/repos/github/JackStat/ModelMetrics/badge.svg?branch=master)](https://coveralls.io/github/JackStat/ModelMetrics?branch=master)
[![Downloads](https://cranlogs.r-pkg.org/badges/ModelMetrics)](https://CRAN.R-project.org/package=ModelMetrics)

%package lib
Summary: lib components for the R-ModelMetrics package.
Group: Libraries

%description lib
lib components for the R-ModelMetrics package.


%prep
%setup -q -c -n ModelMetrics

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571868432

%install
export SOURCE_DATE_EPOCH=1571868432
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ModelMetrics
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ModelMetrics
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ModelMetrics
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ModelMetrics || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ModelMetrics/DESCRIPTION
/usr/lib64/R/library/ModelMetrics/INDEX
/usr/lib64/R/library/ModelMetrics/Meta/Rd.rds
/usr/lib64/R/library/ModelMetrics/Meta/data.rds
/usr/lib64/R/library/ModelMetrics/Meta/features.rds
/usr/lib64/R/library/ModelMetrics/Meta/hsearch.rds
/usr/lib64/R/library/ModelMetrics/Meta/links.rds
/usr/lib64/R/library/ModelMetrics/Meta/nsInfo.rds
/usr/lib64/R/library/ModelMetrics/Meta/package.rds
/usr/lib64/R/library/ModelMetrics/NAMESPACE
/usr/lib64/R/library/ModelMetrics/NEWS.md
/usr/lib64/R/library/ModelMetrics/R/ModelMetrics
/usr/lib64/R/library/ModelMetrics/R/ModelMetrics.rdb
/usr/lib64/R/library/ModelMetrics/R/ModelMetrics.rdx
/usr/lib64/R/library/ModelMetrics/data/Rdata.rdb
/usr/lib64/R/library/ModelMetrics/data/Rdata.rds
/usr/lib64/R/library/ModelMetrics/data/Rdata.rdx
/usr/lib64/R/library/ModelMetrics/help/AnIndex
/usr/lib64/R/library/ModelMetrics/help/ModelMetrics.rdb
/usr/lib64/R/library/ModelMetrics/help/ModelMetrics.rdx
/usr/lib64/R/library/ModelMetrics/help/aliases.rds
/usr/lib64/R/library/ModelMetrics/help/paths.rds
/usr/lib64/R/library/ModelMetrics/html/00Index.html
/usr/lib64/R/library/ModelMetrics/html/R.css
/usr/lib64/R/library/ModelMetrics/tests/testthat.R
/usr/lib64/R/library/ModelMetrics/tests/testthat/test_auc.R
/usr/lib64/R/library/ModelMetrics/tests/testthat/test_calculations.R
/usr/lib64/R/library/ModelMetrics/tests/testthat/test_errors.R
/usr/lib64/R/library/ModelMetrics/tests/testthat/test_logloss.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/ModelMetrics/libs/ModelMetrics.so
/usr/lib64/R/library/ModelMetrics/libs/ModelMetrics.so.avx2
/usr/lib64/R/library/ModelMetrics/libs/ModelMetrics.so.avx512
