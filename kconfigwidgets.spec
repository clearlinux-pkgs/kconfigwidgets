#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v4
# autospec commit: e738c51
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kconfigwidgets
Version  : 6.0.0
Release  : 85
URL      : https://download.kde.org/stable/frameworks/6.0/kconfigwidgets-6.0.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.0/kconfigwidgets-6.0.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.0/kconfigwidgets-6.0.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kconfigwidgets-data = %{version}-%{release}
Requires: kconfigwidgets-lib = %{version}-%{release}
Requires: kconfigwidgets-license = %{version}-%{release}
Requires: kconfigwidgets-locales = %{version}-%{release}
BuildRequires : appstream-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : docbook-xml
BuildRequires : extra-cmake-modules-data
BuildRequires : kauth
BuildRequires : kauth-dev
BuildRequires : kcodecs-dev
BuildRequires : kconfig
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kdoctools-dev
BuildRequires : kguiaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kwidgetsaddons-dev
BuildRequires : libxml2
BuildRequires : libxslt
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KConfigWidgets
Widgets for configuration dialogs
## Introduction
KConfigWidgets provides easy-to-use classes to create configuration dialogs, as
well as a set of widgets which uses KConfig to store their settings.

%package data
Summary: data components for the kconfigwidgets package.
Group: Data

%description data
data components for the kconfigwidgets package.


%package dev
Summary: dev components for the kconfigwidgets package.
Group: Development
Requires: kconfigwidgets-lib = %{version}-%{release}
Requires: kconfigwidgets-data = %{version}-%{release}
Provides: kconfigwidgets-devel = %{version}-%{release}
Requires: kconfigwidgets = %{version}-%{release}

%description dev
dev components for the kconfigwidgets package.


%package lib
Summary: lib components for the kconfigwidgets package.
Group: Libraries
Requires: kconfigwidgets-data = %{version}-%{release}
Requires: kconfigwidgets-license = %{version}-%{release}

%description lib
lib components for the kconfigwidgets package.


%package license
Summary: license components for the kconfigwidgets package.
Group: Default

%description license
license components for the kconfigwidgets package.


%package locales
Summary: locales components for the kconfigwidgets package.
Group: Default

%description locales
locales components for the kconfigwidgets package.


%prep
%setup -q -n kconfigwidgets-6.0.0
cd %{_builddir}/kconfigwidgets-6.0.0

%build
## build_prepend content
# Make sure the package only builds if kdoctools has been updated first
sed -i -r -e 's,(KF.?DocTools \$\{KF.?_DEP_VERSION\})(.*\))$,\1 REQUIRED \2,' CMakeLists.txt || :
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1709308572
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
## build_prepend content
# Make sure the package only builds if kdoctools has been updated first
sed -i -r -e 's,(KF.?DocTools \$\{KF.?_DEP_VERSION\})(.*\))$,\1 REQUIRED \2,' CMakeLists.txt || :
## build_prepend end
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1709308572
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kconfigwidgets
cp %{_builddir}/kconfigwidgets-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kconfigwidgets/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kconfigwidgets-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kconfigwidgets/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/kconfigwidgets-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kconfigwidgets/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kconfigwidgets-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kconfigwidgets/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kconfigwidgets-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kconfigwidgets/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kconfigwidgets-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kconfigwidgets/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kconfigwidgets-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kconfigwidgets/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kconfigwidgets-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kconfigwidgets/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kconfigwidgets6
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/locale/af/kf6_entry.desktop
/usr/share/locale/ar/kf6_entry.desktop
/usr/share/locale/as/kf6_entry.desktop
/usr/share/locale/ast/kf6_entry.desktop
/usr/share/locale/az/kf6_entry.desktop
/usr/share/locale/be/kf6_entry.desktop
/usr/share/locale/be@latin/kf6_entry.desktop
/usr/share/locale/bg/kf6_entry.desktop
/usr/share/locale/bn/kf6_entry.desktop
/usr/share/locale/bn_IN/kf6_entry.desktop
/usr/share/locale/br/kf6_entry.desktop
/usr/share/locale/bs/kf6_entry.desktop
/usr/share/locale/ca/kf6_entry.desktop
/usr/share/locale/ca@valencia/kf6_entry.desktop
/usr/share/locale/crh/kf6_entry.desktop
/usr/share/locale/cs/kf6_entry.desktop
/usr/share/locale/csb/kf6_entry.desktop
/usr/share/locale/cy/kf6_entry.desktop
/usr/share/locale/da/kf6_entry.desktop
/usr/share/locale/de/kf6_entry.desktop
/usr/share/locale/el/kf6_entry.desktop
/usr/share/locale/en_GB/kf6_entry.desktop
/usr/share/locale/en_US/kf6_entry.desktop
/usr/share/locale/eo/kf6_entry.desktop
/usr/share/locale/es/kf6_entry.desktop
/usr/share/locale/et/kf6_entry.desktop
/usr/share/locale/eu/kf6_entry.desktop
/usr/share/locale/fa/kf6_entry.desktop
/usr/share/locale/fi/kf6_entry.desktop
/usr/share/locale/fr/kf6_entry.desktop
/usr/share/locale/fy/kf6_entry.desktop
/usr/share/locale/ga/kf6_entry.desktop
/usr/share/locale/gd/kf6_entry.desktop
/usr/share/locale/gl/kf6_entry.desktop
/usr/share/locale/gu/kf6_entry.desktop
/usr/share/locale/ha/kf6_entry.desktop
/usr/share/locale/he/kf6_entry.desktop
/usr/share/locale/hi/kf6_entry.desktop
/usr/share/locale/hne/kf6_entry.desktop
/usr/share/locale/hr/kf6_entry.desktop
/usr/share/locale/hsb/kf6_entry.desktop
/usr/share/locale/hu/kf6_entry.desktop
/usr/share/locale/hy/kf6_entry.desktop
/usr/share/locale/ia/kf6_entry.desktop
/usr/share/locale/id/kf6_entry.desktop
/usr/share/locale/ie/kf6_entry.desktop
/usr/share/locale/is/kf6_entry.desktop
/usr/share/locale/it/kf6_entry.desktop
/usr/share/locale/ja/kf6_entry.desktop
/usr/share/locale/ka/kf6_entry.desktop
/usr/share/locale/kk/kf6_entry.desktop
/usr/share/locale/km/kf6_entry.desktop
/usr/share/locale/kn/kf6_entry.desktop
/usr/share/locale/ko/kf6_entry.desktop
/usr/share/locale/ku/kf6_entry.desktop
/usr/share/locale/lb/kf6_entry.desktop
/usr/share/locale/lt/kf6_entry.desktop
/usr/share/locale/lv/kf6_entry.desktop
/usr/share/locale/mai/kf6_entry.desktop
/usr/share/locale/mk/kf6_entry.desktop
/usr/share/locale/ml/kf6_entry.desktop
/usr/share/locale/mr/kf6_entry.desktop
/usr/share/locale/ms/kf6_entry.desktop
/usr/share/locale/my/kf6_entry.desktop
/usr/share/locale/nb/kf6_entry.desktop
/usr/share/locale/nds/kf6_entry.desktop
/usr/share/locale/ne/kf6_entry.desktop
/usr/share/locale/nl/kf6_entry.desktop
/usr/share/locale/nn/kf6_entry.desktop
/usr/share/locale/oc/kf6_entry.desktop
/usr/share/locale/or/kf6_entry.desktop
/usr/share/locale/pa/kf6_entry.desktop
/usr/share/locale/pl/kf6_entry.desktop
/usr/share/locale/ps/kf6_entry.desktop
/usr/share/locale/pt/kf6_entry.desktop
/usr/share/locale/pt_BR/kf6_entry.desktop
/usr/share/locale/ro/kf6_entry.desktop
/usr/share/locale/ru/kf6_entry.desktop
/usr/share/locale/se/kf6_entry.desktop
/usr/share/locale/si/kf6_entry.desktop
/usr/share/locale/sk/kf6_entry.desktop
/usr/share/locale/sl/kf6_entry.desktop
/usr/share/locale/sq/kf6_entry.desktop
/usr/share/locale/sr/kf6_entry.desktop
/usr/share/locale/sr@ijekavian/kf6_entry.desktop
/usr/share/locale/sr@ijekavianlatin/kf6_entry.desktop
/usr/share/locale/sr@latin/kf6_entry.desktop
/usr/share/locale/sv/kf6_entry.desktop
/usr/share/locale/ta/kf6_entry.desktop
/usr/share/locale/te/kf6_entry.desktop
/usr/share/locale/tg/kf6_entry.desktop
/usr/share/locale/th/kf6_entry.desktop
/usr/share/locale/tok/kf6_entry.desktop
/usr/share/locale/tr/kf6_entry.desktop
/usr/share/locale/tt/kf6_entry.desktop
/usr/share/locale/ug/kf6_entry.desktop
/usr/share/locale/uk/kf6_entry.desktop
/usr/share/locale/uz/kf6_entry.desktop
/usr/share/locale/uz@cyrillic/kf6_entry.desktop
/usr/share/locale/vi/kf6_entry.desktop
/usr/share/locale/wa/kf6_entry.desktop
/usr/share/locale/xh/kf6_entry.desktop
/usr/share/locale/zh_CN/kf6_entry.desktop
/usr/share/locale/zh_HK/kf6_entry.desktop
/usr/share/locale/zh_TW/kf6_entry.desktop
/usr/share/qlogging-categories6/kconfigwidgets.categories
/usr/share/qlogging-categories6/kconfigwidgets.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KConfigWidgets/KCodecAction
/usr/include/KF6/KConfigWidgets/KColorSchemeMenu
/usr/include/KF6/KConfigWidgets/KCommandBar
/usr/include/KF6/KConfigWidgets/KConfigDialog
/usr/include/KF6/KConfigWidgets/KConfigDialogManager
/usr/include/KF6/KConfigWidgets/KConfigViewStateSaver
/usr/include/KF6/KConfigWidgets/KHamburgerMenu
/usr/include/KF6/KConfigWidgets/KHelpClient
/usr/include/KF6/KConfigWidgets/KLanguageButton
/usr/include/KF6/KConfigWidgets/KLanguageName
/usr/include/KF6/KConfigWidgets/KRecentFilesAction
/usr/include/KF6/KConfigWidgets/KStandardAction
/usr/include/KF6/KConfigWidgets/KViewStateMaintainer
/usr/include/KF6/KConfigWidgets/kcodecaction.h
/usr/include/KF6/KConfigWidgets/kcolorschememenu.h
/usr/include/KF6/KConfigWidgets/kcommandbar.h
/usr/include/KF6/KConfigWidgets/kconfigdialog.h
/usr/include/KF6/KConfigWidgets/kconfigdialogmanager.h
/usr/include/KF6/KConfigWidgets/kconfigviewstatesaver.h
/usr/include/KF6/KConfigWidgets/kconfigwidgets_export.h
/usr/include/KF6/KConfigWidgets/kconfigwidgets_version.h
/usr/include/KF6/KConfigWidgets/khamburgermenu.h
/usr/include/KF6/KConfigWidgets/khelpclient.h
/usr/include/KF6/KConfigWidgets/klanguagebutton.h
/usr/include/KF6/KConfigWidgets/klanguagename.h
/usr/include/KF6/KConfigWidgets/krecentfilesaction.h
/usr/include/KF6/KConfigWidgets/kstandardaction.h
/usr/include/KF6/KConfigWidgets/kviewstatemaintainer.h
/usr/lib64/cmake/KF6ConfigWidgets/KF6ConfigWidgetsConfig.cmake
/usr/lib64/cmake/KF6ConfigWidgets/KF6ConfigWidgetsConfigVersion.cmake
/usr/lib64/cmake/KF6ConfigWidgets/KF6ConfigWidgetsTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6ConfigWidgets/KF6ConfigWidgetsTargets.cmake
/usr/lib64/libKF6ConfigWidgets.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6ConfigWidgets.so.6.0.0
/V3/usr/lib64/qt6/plugins/designer/kconfigwidgets6widgets.so
/usr/lib64/libKF6ConfigWidgets.so.6
/usr/lib64/libKF6ConfigWidgets.so.6.0.0
/usr/lib64/qt6/plugins/designer/kconfigwidgets6widgets.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kconfigwidgets/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kconfigwidgets/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kconfigwidgets/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kconfigwidgets/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kconfigwidgets/e458941548e0864907e654fa2e192844ae90fc32
/usr/share/package-licenses/kconfigwidgets/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f kconfigwidgets6.lang
%defattr(-,root,root,-)

