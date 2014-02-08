Summary:	LZO fast file compressor
Name:		lzop
Version:	1.03
Release:	5
License:	GPLv2+
Group:		Archiving/Compression
Url:		http://www.oberhumer.com/opensource/lzop/
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	liblzo-devel >= 2.00

%description
lzop is a file compressor similar to gzip. Its main advantages over gzip
are much higher compression and decompression speed at the cost
of compression ratio.

lzop was designed with the following goals in mind:
  1) speed (both compression and decompression)
  2) reasonable drop-in compatibility to gzip
  3) portability

%prep
%setup -q

%build
export CPPFLAGS="-D_FILE_OFFSET_BITS=64 -I%_includedir/lzo"
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc README COPYING AUTHORS NEWS THANKS doc/lzop.ps doc/lzop.html
%{_bindir}/lzop
%{_mandir}/man1/lzop.1*

