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
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING AUTHORS NEWS THANKS doc/lzop.ps doc/lzop.html
%_bindir/lzop
%_mandir/man1/lzop.1*


