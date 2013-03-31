Summary:	A GNU collection of diff utilities
Name:		diffutils
Version:	3.3
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/diffutils/%{name}-%{version}.tar.xz
# Source0-md5:	99180208ec2a82ce71f55b0d7389f1b3
URL:		http://www.gnu.org/software/diffutils/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Diffutils includes four utilities: diff, cmp, diff3 and sdiff. Diff
compares two files and shows the differences, line by line. The cmp
command shows the offset and line numbers where two files differ, or
cmp can show the characters that differ between the two files. The
diff3 command shows the differences between three files. Diff3 can be
used when two people have made independent changes to a common
original; diff3 can produce a merged file that contains both persons
changes and warnings about conflicts. The sdiff command can be used to
merge two files interactively.

%prep
%setup -q

%{__sed} -i "/gets is a security hole/d" lib/stdio.in.h

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	PR_PROGRAM=/usr/bin/pr	\
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%if 0
# fails due bashizm
%check
%{__make} -j1 check
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS README
%attr(755,root,root) %{_bindir}/*
%{_infodir}/diffutils.info*
%{_mandir}/man1/*

