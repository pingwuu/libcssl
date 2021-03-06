Summary: Columbo Simple Serial Library
Name: libcssl
Version: 0.9.4
Release: 1
License: LGPL
Group: System Environment/Libraries
URL: http://cssl.sf.net
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Columbo Simple Serial Library is an easy to use, event driven serial port communication library for Linux. 

%prep
%setup -q

%build
make PREFIX=%{_prefix}

%install
make PREFIX=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%dir %{_prefix}/lib
%dir %{_prefix}/include
%dir %{_prefix}/lib/pkgconfig
%{_prefix}/include/cssl.h
%{_prefix}/lib/libcssl.a
%{_prefix}/lib/libcssl.la
%{_prefix}/lib/libcssl.so.0.0.9
%{_prefix}/lib/pkgconfig/libcssl.pc
%doc COPYING README INSTALL


%changelog
* Thu Nov 20 2003 Marcin Siennicki <m.siennicki@cloos.pl> - 
- Initial build.


