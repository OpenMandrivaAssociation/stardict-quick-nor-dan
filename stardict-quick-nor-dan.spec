%define	version	2.4.2
%define release	%mkrel 6
%define dict_format_version	2.4.2

Summary:	Norwegian -> Danish *Quick dictionary for StarDict 2
Name:		stardict-quick-nor-dan
Version:	%{version}
Release:	%{release}
License:	Distributable
Group:		Databases
URL:		http://stardict.sourceforge.net/
Buildroot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildArch:	noarch

Source0:	ftp://osdn.dl.sourceforge.net/pub/sourceforge/s/st/stardict/stardict-quick_nor-dan-%{version}.tar.bz2

Provides:	stardict-dictionary = %{dict_format_version}
Requires:	stardict >= %{dict_format_version}

%description
Norwegian -> Danish *Quick dictionary in StarDict 2 format.
*Quick is an open source translation application. For more info, visit

http://www.futureware.at/.

%prep
%setup -q -n stardict-quick_nor-dan-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/stardict/dic
install -m 0644 * $RPM_BUILD_ROOT%{_datadir}/stardict/dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/stardict/dic/*



%changelog
* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.4.2-6mdv2009.0
+ Revision: 261083
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.4.2-5mdv2009.0
+ Revision: 253369
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.4.2-3mdv2008.1
+ Revision: 140853
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.4.2-3mdv2008.0
+ Revision: 67712
- use %%mkrel


* Sat Oct 01 2005 Abel Cheung <deaddog@mandriva.org> 2.4.2-3mdk
- Rebuild

* Tue Jun 01 2004 Abel Cheung <deaddog@deaddog.org> 2.4.2-2mdk
- Dictionaries require main program as well

* Fri Nov 28 2003 Abel Cheung <deaddog@deaddog.org> 2.4.2-1mdk
- New version
- Conflict with old version of stardict

* Mon Jul 28 2003 Abel Cheung <maddog@linux.org.hk> 2.1.0-1mdk
- First Mandrake style spec

