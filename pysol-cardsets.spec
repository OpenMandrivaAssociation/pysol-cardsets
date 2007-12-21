%define name pysol-cardsets
%define version 4.40
%define release %mkrel 7
%define pysolver 4.81-3mdk

Summary: A collection of free cardsets adapted for use with PySol
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: Games/Cards
URL: http://www.oberhumer.com/opensource/pysol/	
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Requires: pysol >= %pysolver

%description
A collection of 70 free cardsets adapted for use with PySol.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot%_gamesdatadir/pysol
cp -r data/cardset* %buildroot%_gamesdatadir/pysol
cd %buildroot%_gamesdatadir/pysol
rm -rf cardset-2000 cardset-colossus cardset-hard-a-port cardset-hexadeck cardset-kintengu cardset-oxymoron cardset-tuxedo cardset-vienna-2k

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README NEWS
%_gamesdatadir/pysol/*

