%define name lzop
%define version 1.03
%define fversion %version
%define release %mkrel 3

Summary: LZO fast file compressor
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{fversion}.tar.gz
License: GPLv2+
Group: Archiving/Compression
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: liblzo-devel >= 2.00
URL: http://www.oberhumer.com/opensource/lzop/

%description
lzop is a file compressor similar to gzip. Its main advantages over gzip
are much higher compression and decompression speed at the cost
of compression ratio.

lzop was designed with the following goals in mind:
  1) speed (both compression and decompression)
  2) reasonable drop-in compatibility to gzip
  3) portability

%prep
%setup -q -n %name-%fversion

%build
export CPPFLAGS="-D_FILE_OFFSET_BITS=64 -I%_includedir/lzo"
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING AUTHORS NEWS THANKS doc/lzop.ps doc/lzop.html
%_bindir/lzop
%_mandir/man1/lzop.1*




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.03-2mdv2011.0
+ Revision: 666145
- mass rebuild

* Tue Nov 09 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.03-1mdv2011.0
+ Revision: 595424
- new version

* Wed Jan 20 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.02-0.rc1.3mdv2010.1
+ Revision: 494021
- update license

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.02-0.rc1.2mdv2010.0
+ Revision: 426026
- rebuild

* Thu Jan 03 2008 Olivier Blin <oblin@mandriva.com> 1.02-0.rc1.1mdv2008.1
+ Revision: 140934
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed May 16 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.02-0.rc1.1mdv2008.0
+ Revision: 27218
- new version
- drop patch


* Tue Jan 02 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.01-7mdv2007.0
+ Revision: 103086
- Import lzop

* Tue Jan 02 2007 Götz Waschk <waschk@mandriva.org> 1.01-7mdv2007.1
- unpack patch

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.01-6mdk
- Rebuild

* Wed Jun 29 2005 Götz Waschk <waschk@mandriva.org> 1.01-5mdk
- update the patch for new liblzo

* Fri Jun 03 2005 Götz Waschk <waschk@mandriva.org> 1.01-4mdk
- patch for new lzo

* Thu Apr 21 2005 Götz Waschk <waschk@mandriva.org> 1.01-3mdk
- fix large file support (bug #15545)

* Sat May 15 2004 Götz Waschk <waschk@linux-mandrake.com> 1.01-2mdk
- fix buildrequires
- drop prefix

