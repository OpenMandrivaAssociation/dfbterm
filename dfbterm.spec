
%define name dfbterm
%define Name DFBTerm
%define version 0.8.15
%define rel	7
%define release %mkrel %rel

Name:		%name
Summary:	Terminal application for DirectFB
Version:	%version
Release:	%release
URL:		https://www.directfb.org/
Group:		Terminals
Source0:	http://www.directfb.org/downloads/Programs/%{Name}-%{version}.tar.bz2
Patch0:		DFBTerm-0.8.15-fontdir.patch
License:	MIT
BuildRequires:	pkgconfig(directfb)
BuildRequires:	pkgconfig(lite)
BuildRoot:	%{_tmppath}/%{name}-root

%description
DFBTerm is a terminal application for DirectFB. It uses LiTE (LiTE is
a Toolkit Engine) and has a very nice anti aliased fixed width font.

%prep
%setup -q -n %{Name}-%{version}
%patch0 -p0

%build

%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{_sbindir}/dfbterm-pty-helper
%{_bindir}/dfbterm




%changelog
* Fri Dec 17 2010 Funda Wang <fwang@mandriva.org> 0.8.15-7mdv2011.0
+ Revision: 622521
- fix font dir

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Sun Nov 08 2009 Funda Wang <fwang@mandriva.org> 0.8.15-5mdv2010.1
+ Revision: 462941
- rebuild for new dfb

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 0.8.15-4mdv2010.0
+ Revision: 427962
- rebuild

* Thu Aug 21 2008 Funda Wang <fwang@mandriva.org> 0.8.15-3mdv2009.0
+ Revision: 274558
- rebuild

* Fri Dec 28 2007 Anssi Hannula <anssi@mandriva.org> 0.8.15-2mdv2008.1
+ Revision: 138947
- rebuild against new lite

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue May 22 2007 Anssi Hannula <anssi@mandriva.org> 0.8.15-1mdv2008.0
+ Revision: 29846
- 0.8.15


* Sat Mar 03 2007 Anssi Hannula <anssi@mandriva.org> 0.8.0-20051219.3mdv2007.0
+ Revision: 131654
- rebuild
- Import dfbterm

* Sat May 06 2006 Anssi Hannula <anssi@mandriva.org> 0.8.0-20051219.2mdk
- rebuild for new directfb

* Fri Dec 23 2005 Anssi Hannula <anssi@mandriva.org> 0.8.0-20051219.1mdk
- Initial Mandriva package

