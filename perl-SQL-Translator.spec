#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v25
# autospec commit: 9594167
#
Name     : perl-SQL-Translator
Version  : 1.66
Release  : 40
URL      : https://cpan.metacpan.org/authors/id/V/VE/VEESH/SQL-Translator-1.66.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/V/VE/VEESH/SQL-Translator-1.66.tar.gz
Summary  : 'SQL DDL transformations and more'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-SQL-Translator-bin = %{version}-%{release}
Requires: perl-SQL-Translator-man = %{version}-%{release}
Requires: perl-SQL-Translator-perl = %{version}-%{release}
Requires: perl(GD)
BuildRequires : buildreq-cpan
BuildRequires : perl(Algorithm::Diff)
BuildRequires : perl(Carp::Clan)
BuildRequires : perl(Class::Method::Modifiers)
BuildRequires : perl(DBI)
BuildRequires : perl(File::ShareDir)
BuildRequires : perl(File::ShareDir::Install)
BuildRequires : perl(Import::Into)
BuildRequires : perl(JSON::MaybeXS)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Moo)
BuildRequires : perl(Package::Variant)
BuildRequires : perl(Parse::RecDescent)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(Sub::Quote)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Differences)
BuildRequires : perl(Test::Exception)
BuildRequires : perl(Text::Diff)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(XML::Writer)
BuildRequires : perl(YAML)
BuildRequires : perl(strictures)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
SQL::Translator - manipulate structured data definitions (SQL and more)
SYNOPSIS
use SQL::Translator;

%package bin
Summary: bin components for the perl-SQL-Translator package.
Group: Binaries

%description bin
bin components for the perl-SQL-Translator package.


%package dev
Summary: dev components for the perl-SQL-Translator package.
Group: Development
Requires: perl-SQL-Translator-bin = %{version}-%{release}
Provides: perl-SQL-Translator-devel = %{version}-%{release}
Requires: perl-SQL-Translator = %{version}-%{release}

%description dev
dev components for the perl-SQL-Translator package.


%package man
Summary: man components for the perl-SQL-Translator package.
Group: Default

%description man
man components for the perl-SQL-Translator package.


%package perl
Summary: perl components for the perl-SQL-Translator package.
Group: Default
Requires: perl-SQL-Translator = %{version}-%{release}

%description perl
perl components for the perl-SQL-Translator package.


%prep
%setup -q -n SQL-Translator-1.66
cd %{_builddir}/SQL-Translator-1.66
pushd ..
cp -a SQL-Translator-1.66 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sqlt
/usr/bin/sqlt-diagram
/usr/bin/sqlt-diff
/usr/bin/sqlt-diff-old
/usr/bin/sqlt-dumper
/usr/bin/sqlt-graph

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/SQL::Translator.3
/usr/share/man/man3/SQL::Translator::Diff.3
/usr/share/man/man3/SQL::Translator::Filter::DefaultExtra.3
/usr/share/man/man3/SQL::Translator::Filter::Globals.3
/usr/share/man/man3/SQL::Translator::Filter::Names.3
/usr/share/man/man3/SQL::Translator::Generator::DDL::MySQL.3
/usr/share/man/man3/SQL::Translator::Generator::DDL::PostgreSQL.3
/usr/share/man/man3/SQL::Translator::Generator::DDL::SQLServer.3
/usr/share/man/man3/SQL::Translator::Generator::DDL::SQLite.3
/usr/share/man/man3/SQL::Translator::Generator::Role::DDL.3
/usr/share/man/man3/SQL::Translator::Generator::Role::Quote.3
/usr/share/man/man3/SQL::Translator::Manual.3
/usr/share/man/man3/SQL::Translator::Parser.3
/usr/share/man/man3/SQL::Translator::Parser::Access.3
/usr/share/man/man3/SQL::Translator::Parser::DB2.3
/usr/share/man/man3/SQL::Translator::Parser::DBI.3
/usr/share/man/man3/SQL::Translator::Parser::DBI::DB2.3
/usr/share/man/man3/SQL::Translator::Parser::DBI::MySQL.3
/usr/share/man/man3/SQL::Translator::Parser::DBI::Oracle.3
/usr/share/man/man3/SQL::Translator::Parser::DBI::PostgreSQL.3
/usr/share/man/man3/SQL::Translator::Parser::DBI::SQLServer.3
/usr/share/man/man3/SQL::Translator::Parser::DBI::SQLite.3
/usr/share/man/man3/SQL::Translator::Parser::DBI::Sybase.3
/usr/share/man/man3/SQL::Translator::Parser::Excel.3
/usr/share/man/man3/SQL::Translator::Parser::JSON.3
/usr/share/man/man3/SQL::Translator::Parser::MySQL.3
/usr/share/man/man3/SQL::Translator::Parser::Oracle.3
/usr/share/man/man3/SQL::Translator::Parser::PostgreSQL.3
/usr/share/man/man3/SQL::Translator::Parser::SQLServer.3
/usr/share/man/man3/SQL::Translator::Parser::SQLite.3
/usr/share/man/man3/SQL::Translator::Parser::Storable.3
/usr/share/man/man3/SQL::Translator::Parser::Sybase.3
/usr/share/man/man3/SQL::Translator::Parser::XML.3
/usr/share/man/man3/SQL::Translator::Parser::XML::SQLFairy.3
/usr/share/man/man3/SQL::Translator::Parser::YAML.3
/usr/share/man/man3/SQL::Translator::Parser::xSV.3
/usr/share/man/man3/SQL::Translator::Producer.3
/usr/share/man/man3/SQL::Translator::Producer::ClassDBI.3
/usr/share/man/man3/SQL::Translator::Producer::DB2.3
/usr/share/man/man3/SQL::Translator::Producer::DiaUml.3
/usr/share/man/man3/SQL::Translator::Producer::Diagram.3
/usr/share/man/man3/SQL::Translator::Producer::Dumper.3
/usr/share/man/man3/SQL::Translator::Producer::GraphViz.3
/usr/share/man/man3/SQL::Translator::Producer::HTML.3
/usr/share/man/man3/SQL::Translator::Producer::JSON.3
/usr/share/man/man3/SQL::Translator::Producer::Latex.3
/usr/share/man/man3/SQL::Translator::Producer::MySQL.3
/usr/share/man/man3/SQL::Translator::Producer::Oracle.3
/usr/share/man/man3/SQL::Translator::Producer::POD.3
/usr/share/man/man3/SQL::Translator::Producer::PostgreSQL.3
/usr/share/man/man3/SQL::Translator::Producer::SQLServer.3
/usr/share/man/man3/SQL::Translator::Producer::SQLite.3
/usr/share/man/man3/SQL::Translator::Producer::Storable.3
/usr/share/man/man3/SQL::Translator::Producer::Sybase.3
/usr/share/man/man3/SQL::Translator::Producer::TT::Base.3
/usr/share/man/man3/SQL::Translator::Producer::TT::Table.3
/usr/share/man/man3/SQL::Translator::Producer::TTSchema.3
/usr/share/man/man3/SQL::Translator::Producer::XML.3
/usr/share/man/man3/SQL::Translator::Producer::XML::SQLFairy.3
/usr/share/man/man3/SQL::Translator::Producer::YAML.3
/usr/share/man/man3/SQL::Translator::Role::BuildArgs.3
/usr/share/man/man3/SQL::Translator::Role::Error.3
/usr/share/man/man3/SQL::Translator::Role::ListAttr.3
/usr/share/man/man3/SQL::Translator::Schema.3
/usr/share/man/man3/SQL::Translator::Schema::Constants.3
/usr/share/man/man3/SQL::Translator::Schema::Constraint.3
/usr/share/man/man3/SQL::Translator::Schema::Field.3
/usr/share/man/man3/SQL::Translator::Schema::Index.3
/usr/share/man/man3/SQL::Translator::Schema::IndexField.3
/usr/share/man/man3/SQL::Translator::Schema::Object.3
/usr/share/man/man3/SQL::Translator::Schema::Procedure.3
/usr/share/man/man3/SQL::Translator::Schema::Role::Compare.3
/usr/share/man/man3/SQL::Translator::Schema::Role::Extra.3
/usr/share/man/man3/SQL::Translator::Schema::Table.3
/usr/share/man/man3/SQL::Translator::Schema::Trigger.3
/usr/share/man/man3/SQL::Translator::Schema::View.3
/usr/share/man/man3/SQL::Translator::Types.3
/usr/share/man/man3/SQL::Translator::Utils.3
/usr/share/man/man3/Test::SQL::Translator.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/sqlt-diagram.1
/usr/share/man/man1/sqlt-diff-old.1
/usr/share/man/man1/sqlt-diff.1
/usr/share/man/man1/sqlt-dumper.1
/usr/share/man/man1/sqlt-graph.1
/usr/share/man/man1/sqlt.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
