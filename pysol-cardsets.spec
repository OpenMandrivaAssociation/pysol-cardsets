%define name pysol-cardsets
%define version 4.40
%define release 12
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



%changelog
* Thu Aug 04 2011 GÃ¶tz Waschk <waschk@mandriva.org> 4.40-11mdv2012.0
+ Revision: 693152
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 4.40-10mdv2011.0
+ Revision: 259473
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 4.40-9mdv2009.0
+ Revision: 247328
- rebuild

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 4.40-7mdv2008.1
+ Revision: 136447
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Jun 06 2006 GÃ¶tz Waschk <waschk@mandriva.org> 4.40-7mdk
- Rebuild
- use mkrel

* Fri Jun 03 2005 Götz Waschk <waschk@mandriva.org> 4.40-6mdk
- drop prefix
- remove the cardsets already in the main package

* Fri Aug 13 2004 Götz Waschk <waschk@linux-mandrake.com> 4.40-5mdk
- rebuild

* Mon Jul 07 2003 Götz Waschk <waschk@linux-mandrake.com> 4.40-4mdk
- move files around (fixes bug 4153)

