#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Devel
%define		pnam	StackTrace-AsHTML
%include	/usr/lib/rpm/macros.perl
Summary:	Devel::StackTrace::AsHTML - Displays stack trace in HTML
#Summary(pl.UTF-8):	
Name:		perl-Devel-StackTrace-AsHTML
Version:	0.11
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	46ff8282d671f63e6a5f48bf45d86bbb
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Devel-StackTrace-AsHTML/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Devel-StackTrace
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::StackTrace::AsHTML adds as_html method to Devel::StackTrace which
displays the stack trace in beautiful HTML, with code snippet context and
function parameters. If you call it on an instance of
Devel::StackTrace::WithLexicals, you even get to see the lexical variables
of each stack frame.



# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Devel/StackTrace/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
