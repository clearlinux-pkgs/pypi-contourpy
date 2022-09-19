#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-contourpy
Version  : 1.0.5
Release  : 1
URL      : https://files.pythonhosted.org/packages/38/b3/d6fd43ab2eadce72ac089328d80e9cdf274efdb79a9933aaf52ef1621e99/contourpy-1.0.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/38/b3/d6fd43ab2eadce72ac089328d80e9cdf274efdb79a9933aaf52ef1621e99/contourpy-1.0.5.tar.gz
Summary  : Python library for calculating contours of 2D quadrilateral grids
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-contourpy-filemap = %{version}-%{release}
Requires: pypi-contourpy-lib = %{version}-%{release}
Requires: pypi-contourpy-python = %{version}-%{release}
Requires: pypi-contourpy-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(build)
BuildRequires : pypi(numpy)
BuildRequires : pypi(pybind11)
BuildRequires : pypi(setuptools)

%description
<img alt="ContourPy" src="https://raw.githubusercontent.com/contourpy/contourpy/main/docs/_static/contourpy_logo_horiz.svg" height="90">

%package filemap
Summary: filemap components for the pypi-contourpy package.
Group: Default

%description filemap
filemap components for the pypi-contourpy package.


%package lib
Summary: lib components for the pypi-contourpy package.
Group: Libraries
Requires: pypi-contourpy-filemap = %{version}-%{release}

%description lib
lib components for the pypi-contourpy package.


%package python
Summary: python components for the pypi-contourpy package.
Group: Default
Requires: pypi-contourpy-python3 = %{version}-%{release}

%description python
python components for the pypi-contourpy package.


%package python3
Summary: python3 components for the pypi-contourpy package.
Group: Default
Requires: pypi-contourpy-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(contourpy)
Requires: pypi(numpy)

%description python3
python3 components for the pypi-contourpy package.


%prep
%setup -q -n contourpy-1.0.5
cd %{_builddir}/contourpy-1.0.5
pushd ..
cp -a contourpy-1.0.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663611935
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-contourpy

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*