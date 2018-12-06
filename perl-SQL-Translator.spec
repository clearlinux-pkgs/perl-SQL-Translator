#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-SQL-Translator
Version  : 0.11024
Release  : 8
URL      : https://cpan.metacpan.org/authors/id/I/IL/ILMARI/SQL-Translator-0.11024.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/I/IL/ILMARI/SQL-Translator-0.11024.tar.gz
Summary  : 'SQL DDL transformations and more'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-SQL-Translator-bin = %{version}-%{release}
Requires: perl-SQL-Translator-man = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Carp::Clan)
BuildRequires : perl(Class::Method::Modifiers)
BuildRequires : perl(DBI)
BuildRequires : perl(Devel::GlobalDestruction)
BuildRequires : perl(File::ShareDir)
BuildRequires : perl(Import::Into)
BuildRequires : perl(JSON)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Moo)
BuildRequires : perl(Package::Variant)
BuildRequires : perl(Parse::RecDescent)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Quote)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Differences)
BuildRequires : perl(Test::Exception)
BuildRequires : perl(Text::Diff)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(XML::Writer)
BuildRequires : perl(YAML)
BuildRequires : perl(strictures)

%description
NAME
SQL::Translator - manipulate structured data definitions (SQL and more)
SYNOPSIS
use SQL::Translator;

%package bin
Summary: bin components for the perl-SQL-Translator package.
Group: Binaries
Requires: perl-SQL-Translator-man = %{version}-%{release}

%description bin
bin components for the perl-SQL-Translator package.


%package dev
Summary: dev components for the perl-SQL-Translator package.
Group: Development
Requires: perl-SQL-Translator-bin = %{version}-%{release}
Provides: perl-SQL-Translator-devel = %{version}-%{release}

%description dev
dev components for the perl-SQL-Translator package.


%package man
Summary: man components for the perl-SQL-Translator package.
Group: Default

%description man
man components for the perl-SQL-Translator package.


%prep
%setup -q -n SQL-Translator-0.11024

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
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

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Diff.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Filter/DefaultExtra.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Filter/Globals.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Filter/Names.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Generator/DDL/MySQL.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Generator/DDL/PostgreSQL.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Generator/DDL/SQLServer.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Generator/DDL/SQLite.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Generator/Role/DDL.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Generator/Role/Quote.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Manual.pod
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/Access.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/DB2.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/DB2/Grammar.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/DBI.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/DBI/DB2.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/DBI/MySQL.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/DBI/Oracle.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/DBI/PostgreSQL.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/DBI/SQLServer.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/DBI/SQLite.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/DBI/Sybase.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/Excel.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/JSON.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/MySQL.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/Oracle.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/PostgreSQL.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/SQLServer.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/SQLite.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/Storable.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/Sybase.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/XML.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/XML/SQLFairy.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/YAML.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Parser/xSV.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/ClassDBI.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/DB2.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/DiaUml.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/Diagram.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/Dumper.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/GraphViz.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/HTML.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/JSON.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/Latex.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/MySQL.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/Oracle.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/POD.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/PostgreSQL.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/SQLServer.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/SQLite.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/Storable.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/Sybase.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/TT/Base.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/TT/Table.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/TTSchema.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/XML.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/XML/SQLFairy.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Producer/YAML.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Role/BuildArgs.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Role/Debug.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Role/Error.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Role/ListAttr.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Schema.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Schema/Constants.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Schema/Constraint.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Schema/Field.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Schema/Index.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Schema/Object.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Schema/Procedure.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Schema/Role/Compare.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Schema/Role/Extra.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Schema/Table.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Schema/Trigger.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Schema/View.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Types.pm
/usr/lib/perl5/vendor_perl/5.28.1/SQL/Translator/Utils.pm
/usr/lib/perl5/vendor_perl/5.28.1/Test/SQL/Translator.pm
/usr/lib/perl5/vendor_perl/5.28.1/auto/share/dist/SQL-Translator/DiaUml/diagram.tt2
/usr/lib/perl5/vendor_perl/5.28.1/auto/share/dist/SQL-Translator/DiaUml/layer.tt2
/usr/lib/perl5/vendor_perl/5.28.1/auto/share/dist/SQL-Translator/DiaUml/schema.tt2
/usr/lib/perl5/vendor_perl/5.28.1/auto/share/dist/SQL-Translator/DiaUml/uml-attribute.tt2
/usr/lib/perl5/vendor_perl/5.28.1/auto/share/dist/SQL-Translator/DiaUml/uml-class-all.tt2
/usr/lib/perl5/vendor_perl/5.28.1/auto/share/dist/SQL-Translator/DiaUml/uml-class-end.tt2
/usr/lib/perl5/vendor_perl/5.28.1/auto/share/dist/SQL-Translator/DiaUml/uml-class-start.tt2
/usr/lib/perl5/vendor_perl/5.28.1/auto/share/dist/SQL-Translator/DiaUml/uml-class.tt2
/usr/lib/perl5/vendor_perl/5.28.1/auto/share/dist/SQL-Translator/PrecompiledParsers/Parse/RecDescent/DDL/SQLT/README

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
