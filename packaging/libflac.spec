%define prefix  /usr

Name:       libflac
Summary:    An Open Source lossless audio codec
Version:    1.2.1+slp2+build02
Release:    release 1
Group:      Libraries/Sound
License:    BSD
URL:        http://flac.sourceforge.net/
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: libogg
BuildRequires: gettext

%description
An Open Source lossless audio codec

%package devel
Summary: an open source lossless audio codec
Group: Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
an open source lossless audio codec

%prep
%setup -q

%build
./autogen.sh --prefix=%{prefix}
make

%install
if [ -d %{buildroot} ]; then rm -rf %{buildroot}; fi
mkdir -p %{buildroot}$
make install DESTDIR=%{buildroot}

%clean
if [ -d %{buildroot} ]; then rm -rf %{buildroot}; fi

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING.GPL COPYING.LGPL COPYING.Xiph README
%prefix/lib/libFLAC.so.*

%files devel
%defattr(-,root,root,-)
%{prefix}/include/*
%{prefix}/lib/lib*.la
%{prefix}/lib/lib*.a
%{prefix}/lib/libFLAC.so
%{prefix}/lib/libFLAC++.so*
%{prefix}/lib/pkgconfig/*

%exclude
/usr/bin/flac
/usr/bin/metaflac
/usr/share/aclocal/libFLAC++.m4
/usr/share/aclocal/libFLAC.m4
/usr/share/man/man1/flac.1.gz
/usr/share/man/man1/metaflac.1.gz
