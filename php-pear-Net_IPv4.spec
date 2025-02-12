%define		_class		Net
%define		_subclass	IPv4
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.3.4
Release:	5
Summary:	IPv4 network calculations and validation
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Net_IPv4/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Class used for calculating IPv4 (AF_INET family) address information
such as network addresses as well as IP address validity.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-3mdv2012.0
+ Revision: 742146
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3.4-2
+ Revision: 679428
- mass rebuild

* Thu Sep 09 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.4-1mdv2011.0
+ Revision: 576925
- update to new version 1.3.4

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.2-1mdv2011.0
+ Revision: 569599
- update to new version 1.3.2

* Sun Nov 22 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.1-4mdv2010.1
+ Revision: 468704
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Nov 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.1-3mdv2010.1
+ Revision: 463812
- use rpm filetriggers to register starting from mandriva 2010.1

* Thu Oct 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.1-2mdv2010.0
+ Revision: 452036
- fix %%postun

* Sun Sep 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.3.1-1mdv2010.0
+ Revision: 450230
- new version
- use pear installer
- use fedora %%post/%%postun

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.3.0-4mdv2010.0
+ Revision: 441450
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-3mdv2009.1
+ Revision: 322431
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-2mdv2009.0
+ Revision: 236985
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-1mdv2007.0
+ Revision: 82320
- Import php-pear-Net_IPv4

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.3.0-1mdk
- 1.3.0
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2-5mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2-4mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2-3mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2-2mdk
- fix spec file to conform with the others

* Sat May 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2-1mdk
- initial Mandriva package

