
%define name dfbterm
%define Name DFBTerm
%define version 0.8.0
%define rel	3
%define release %mkrel 20051219.%rel

%define cvssnap 2005-12-19-05-25-07-UTC

Name:		%name
Summary:	Terminal application for DirectFB
Version:	%version
Release:	%release
URL:		http://www.directfb.org/
Group:		Terminals
Source0:	http://www.directfb.org/snapshots/%{Name}-%{cvssnap}.tar.bz2
License:	MIT
BuildRequires:	directfb-devel
BuildRequires:	lite-devel
BuildRequires:	automake
BuildRoot:	%{_tmppath}/%{name}-root

%description
DFBTerm is a terminal application for DirectFB. It uses LiTE (LiTE is
a Toolkit Engine) and has a very nice anti aliased fixed width font.

%prep
%setup -q -n %{Name}-%{cvssnap}

%build

./autogen.sh
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


