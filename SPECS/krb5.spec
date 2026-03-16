%global package_speccommit b8f75e22abb0efecc7788d08b5e4747a73c3a9da
%global usver 1.21.3
%global xsver 4
%global xsrel %{xsver}%{?xscount}%{?xshash}
# Set this so that find-lang.sh will recognize the .po files.
%global gettext_domain mit-krb5
# Guess where the -libs subpackage's docs are going to go.
%define libsdocdir %{?_pkgdocdir:%(echo %{_pkgdocdir} | sed -e s,krb5,krb5-libs,g)}%{!?_pkgdocdir:%{_docdir}/%{name}-libs-%{version}}
# Figure out where the default ccache lives and how we set it.
%global configure_default_ccache_name 1
%global configured_default_ccache_name KEYRING:persistent:%%{uid}

# Use baserelease to set the release number!
#
# baserelease is what we have standardized across Fedora and what
# rpmdev-bumpspec knows how to handle.
%global baserelease 3

# This should be e.g. beta1 or %%nil
%global pre_release %nil

%global krb5_release %{baserelease}
%if "x%{?pre_release}" != "x"
%global krb5_release 0.%{baserelease}.%{pre_release}
%global krb5_pre_release -%{pre_release}
%endif

%global krb5_version_major 1
%global krb5_version_minor 21
# For a release without a patch number set to %%nil
%global krb5_version_patch 3

%global krb5_version_major_minor %{krb5_version_major}.%{krb5_version_minor}
%global krb5_version %{krb5_version_major_minor}
%if "x%{?krb5_version_patch}" != "x"
%global krb5_version %{krb5_version_major_minor}.%{krb5_version_patch}
%endif

# Should be in form 5.0, 6.1, etc.
%global kdbversion 9.0

%if 0%{?xenserver} > 8
%bcond_without docs
%bcond_without crypto_policies
%bcond_with devtoolset
%else
# XS8 gcc is not up to date, use devtoolset instead
%bcond_without devtoolset
%bcond_with docs
# XS8 does not have system level crypto-policies
%bcond_with crypto_policies
%endif

Summary: The Kerberos network authentication system
Name: krb5
Version: %{krb5_version}
Release: %{?xsrel}.1%{?dist}

# rharwood has trust path to signing key and verifies on check-in
Source0: krb5-1.21.3.tar.gz
Source2: kprop.service
Source3: kadmin.service
Source4: krb5kdc.service
Source5: krb5.conf
Source6: kdc.conf
Source7: kadm5.acl
Source8: krb5kdc.sysconfig
Source9: kadmin.sysconfig
Source10: kprop.sysconfig
Source11: ksu.pamd
Source12: krb5kdc.logrotate
Source13: kadmind.logrotate
Source14: krb5-krb5kdc.conf
Source50: krb5-xs.conf
Patch0: 0001-downstream-Revert-Don-t-issue-session-keys-with-depr.patch
Patch1: 0002-downstream-ksu-pam-integration.patch
Patch2: 0003-downstream-SELinux-integration.patch
Patch3: 0004-downstream-fix-debuginfo-with-y.tab.c.patch
Patch4: 0005-downstream-Remove-3des-support.patch
Patch5: 0006-downstream-FIPS-with-PRNG-and-RADIUS-and-MD4.patch
Patch6: 0007-downstream-Allow-krad-UDP-TCP-localhost-connection-w.patch
Patch7: 0008-downstream-Make-tests-compatible-with-sssd_krb5_loca.patch
Patch8: 0009-downstream-Include-missing-OpenSSL-FIPS-header.patch
Patch9: 0010-downstream-Do-not-set-root-as-ksu-file-owner.patch
Patch10: 0011-downstream-Allow-KRB5KDF-MD5-and-MD4-in-FIPS-mode.patch
Patch11: 0012-downstream-Allow-to-set-PAC-ticket-signature-as-opti.patch
Patch12: 0013-downstream-Make-PKINIT-CMS-SHA-1-signature-verificat.patch
Patch13: 0014-Enable-PKINIT-if-at-least-one-group-is-available.patch
Patch14: 0015-Replace-ssl.wrap_socket-for-tests.patch
Patch15: 0016-Eliminate-old-style-function-declarations.patch
Patch16: 0017-Fix-two-unlikely-memory-leaks.patch
Patch17: 0018-Fix-unimportant-memory-leaks.patch
Patch18: 0019-Remove-klist-s-defname-global-variable.patch
Patch19: 0020-End-connection-on-KDC_ERR_SVC_UNAVAILABLE.patch
Patch20: 0021-Add-request_timeout-configuration-parameter.patch
Patch21: 0022-Wait-indefinitely-on-KDC-TCP-connections.patch
Patch22: 0023-Remove-PKINIT-RSA-support.patch
Patch23: 0024-Fix-various-issues-detected-by-static-analysis.patch
Patch24: 0025-Generate-and-verify-message-MACs-in-libkrad.patch
Patch25: Disable-_kerberos-master-SRV-query-for-AD.patch

License: Brian-Gladman-2-Clause AND BSD-2-Clause AND (BSD-2-Clause OR GPL-2.0-or-later) AND BSD-2-Clause-first-lines AND BSD-3-Clause AND BSD-4-Clause AND CMU-Mach-nodoc AND FSFULLRWD AND HPND AND HPND-export2-US AND HPND-export-US AND HPND-export-US-acknowledgement AND HPND-export-US-modify AND ISC AND MIT AND MIT-CMU AND OLDAP-2.8 AND OpenVision
URL: https://web.mit.edu/kerberos/www/
BuildRequires: autoconf, bison, make, flex, gawk, gettext, pkgconfig, sed
%if %{with devtoolset}
BuildRequires: devtoolset-11-gcc, devtoolset-11-gcc-c++
%else
BuildRequires: gcc, gcc-c++
%endif
BuildRequires: libcom_err-devel, libedit-devel, libss-devel
BuildRequires: gzip, ncurses-devel
%if %{with docs}
BuildRequires: python3-sphinx python3
%endif
BuildRequires: keyutils, keyutils-libs-devel >= 1.5.8
BuildRequires: pam-devel
BuildRequires: systemd-units
BuildRequires: tcl-devel
BuildRequires: libverto-devel
BuildRequires: openldap-devel
BuildRequires: lmdb-devel
BuildRequires: perl-interpreter

# For autosetup
BuildRequires: git

BuildRequires: openssl-devel >= 0:3.0.0

%description
Kerberos V5 is a trusted-third-party network authentication system,
which can improve your network's security by eliminating the insecure
practice of sending passwords over the network in unencrypted form.

%package devel
Summary: Development files needed to compile Kerberos 5 programs
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: libkadm5%{?_isa} = %{version}-%{release}
Requires: libcom_err-devel
Requires: keyutils-libs-devel
Requires: libverto-devel
Provides: krb5-kdb-devel-version = %{kdbversion}
# IPA wants ^ to be a separate symbol because they don't trust package
# managers to match -server and -devel in version.  Just go with it.

%description devel
Kerberos is a network authentication system. The krb5-devel package
contains the header files and libraries needed for compiling Kerberos
5 programs. If you want to develop Kerberos-aware programs, you need
to install this package.

%package libs
Summary: The non-admin shared libraries used by Kerberos 5
Requires: openssl-libs >= 0:3.0.0
Requires: coreutils, gawk, sed
Requires: keyutils-libs >= 1.5.8
%if %{with crypto_policies}
Requires: /etc/crypto-policies/back-ends/krb5.config
%endif


%description libs
Kerberos is a network authentication system. The krb5-libs package
contains the shared libraries needed by Kerberos 5. If you are using
Kerberos, you need to install this package.

%package server
Summary: The KDC and related programs for Kerberos 5
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-pkinit%{?_isa} = %{version}-%{release}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
# we drop files in its directory, but we don't want to own that directory
Requires: logrotate
# for run-time, and for parts of the test suite
BuildRequires: libverto-module-base
Requires: libverto-module-base
Requires: libkadm5%{?_isa} = %{version}-%{release}
Provides: krb5-kdb-version = %{kdbversion}

%description server
Kerberos is a network authentication system. The krb5-server package
contains the programs that must be installed on a Kerberos 5 key
distribution center (KDC).  If you are installing a Kerberos 5 KDC,
you need to install this package (in other words, most people should
NOT install this package).

%package server-ldap
Summary: The LDAP storage plugin for the Kerberos 5 KDC
Requires: %{name}-server%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: libkadm5%{?_isa} = %{version}-%{release}

%description server-ldap
Kerberos is a network authentication system. The krb5-server package
contains the programs that must be installed on a Kerberos 5 key
distribution center (KDC).  If you are installing a Kerberos 5 KDC,
and you wish to use a directory server to store the data for your
realm, you need to install this package.

%package workstation
Summary: Kerberos 5 programs for use on workstations
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-pkinit%{?_isa} = %{version}-%{release}
Requires: libkadm5%{?_isa} = %{version}-%{release}

%description workstation
Kerberos is a network authentication system. The krb5-workstation
package contains the basic Kerberos programs (kinit, klist, kdestroy,
kpasswd). If your network uses Kerberos, this package should be
installed on every workstation.

%package pkinit
Summary: The PKINIT module for Kerberos 5
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes: krb5-pkinit-openssl < %{version}-%{release}
Provides: krb5-pkinit-openssl = %{version}-%{release}

%description pkinit
Kerberos is a network authentication system. The krb5-pkinit
package contains the PKINIT plugin, which allows clients
to obtain initial credentials from a KDC using a private key and a
certificate.

%package -n libkadm5
Summary: Kerberos 5 Administrative libraries
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description -n libkadm5
Kerberos is a network authentication system. The libkadm5 package
contains only the libkadm5clnt and libkadm5serv shared objects. This
interface is not considered stable.

%prep
%if %{with devtoolset}
source /opt/rh/devtoolset-11/enable
%endif
%autosetup -S git_am -n %{name}-%{version}%{?dashpre}
ln NOTICE LICENSE

# Generate an FDS-compatible LDIF file.
inldif=src/plugins/kdb/ldap/libkdb_ldap/kerberos.ldif
cat > '60kerberos.ldif' << EOF
# This is a variation on kerberos.ldif which 389 Directory Server will like.
dn: cn=schema
EOF
grep -Eiv '(^$|^dn:|^changetype:|^add:)' $inldif >> 60kerberos.ldif
touch -r $inldif 60kerberos.ldif

# Rebuild the configure scripts.
pushd src
autoreconf -fiv
popd

# Mess with some of the default ports that we use for testing, so that multiple
# builds going on the same host don't step on each other.
cfg="src/util/k5test.py"
LONG_BIT=`getconf LONG_BIT`
PORT=`expr 61000 + $LONG_BIT - 48`
sed -i -e s,61000,`expr "$PORT" + 0`,g $cfg
PORT=`expr 1750 + $LONG_BIT - 48`
sed -i -e s,1750,`expr "$PORT" + 0`,g $cfg
sed -i -e s,1751,`expr "$PORT" + 1`,g $cfg
sed -i -e s,1752,`expr "$PORT" + 2`,g $cfg
PORT=`expr 8888 + $LONG_BIT - 48`
sed -i -e s,8888,`expr "$PORT" - 0`,g $cfg
sed -i -e s,8887,`expr "$PORT" - 1`,g $cfg
sed -i -e s,8886,`expr "$PORT" - 2`,g $cfg
PORT=`expr 7777 + $LONG_BIT - 48`
sed -i -e s,7777,`expr "$PORT" + 0`,g $cfg
sed -i -e s,7778,`expr "$PORT" + 1`,g $cfg

# Fix kadmind port hard-coded in tests
PORT=`expr 61000 + $LONG_BIT - 48`
sed -i -e \
    "s,params.kadmind_port = 61001;,params.kadmind_port = $((PORT + 1));," \
    src/lib/kadm5/t_kadm5.c


%build
%if %{with devtoolset}
source /opt/rh/devtoolset-11/enable
%endif
# Go ahead and supply tcl info, because configure doesn't know how to find it.
source %{_libdir}/tclConfig.sh
pushd src

# This should be safe to remove once we have autoconf >= 2.70
export runstatedir=/run

# Work out the CFLAGS and CPPFLAGS which we intend to use.
INCLUDES=-I%{_includedir}/et
CFLAGS="`echo $RPM_OPT_FLAGS $DEFINES $INCLUDES -fPIC -fno-strict-aliasing -fstack-protector-all`"
CPPFLAGS="`echo $DEFINES $INCLUDES`"
%configure \
    CC="%{__cc}" \
    CFLAGS="$CFLAGS" \
    CPPFLAGS="$CPPFLAGS" \
    SS_LIB="-lss" \
    PKCS11_MODNAME="p11-kit-proxy.so" \
    --enable-shared \
    --runstatedir=/run \
    --localstatedir=%{_var}/kerberos \
    --disable-rpath \
    --without-krb5-config \
    --with-system-et \
    --with-system-ss \
    --with-tcl \
    --enable-dns-for-realm \
    --with-ldap \
    --with-dirsrv-account-locking \
    --enable-pkinit \
    --with-crypto-impl=openssl \
    --with-tls-impl=openssl \
    --with-system-verto \
    --with-pam \
    --without-selinux \
    --with-prng-alg=os \
    --with-lmdb \
    || (cat config.log; exit 1)

# Check we have required features enabled
for x in DNS_LOOKUP DNS_LOOKUP_REALM; do
    grep -q "#define KRB5_${x} 1" include/autoconf.h
done

# Sanity check the KDC_RUN_DIR.
pushd include
make osconf.h
popd
configured_dir=`grep KDC_RUN_DIR include/osconf.h | awk '{print $NF}'`
configured_dir=`eval echo $configured_dir`
if test "$configured_dir" != /run/krb5kdc ; then
    echo Failed to configure KDC_RUN_DIR.
    exit 1
fi

# Build fast, but get better errors if we fail
make %{?_smp_mflags} || make -j1
popd

# Build the docs.
%if %{with docs}
make -C src/doc paths.py version.py
cp src/doc/paths.py doc/
mkdir -p build-man build-html
sphinx-build -a -b man   -t pathsubs doc build-man
sphinx-build -a -b html  -t pathsubs doc build-html
rm -fr build-html/_sources
%endif

%install
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf -- "$RPM_BUILD_ROOT"

# Sample KDC config files (bundled kdc.conf and kadm5.acl).
mkdir -p $RPM_BUILD_ROOT%{_var}/kerberos/krb5kdc
install -pm 600 %{SOURCE6} $RPM_BUILD_ROOT%{_var}/kerberos/krb5kdc/
install -pm 600 %{SOURCE7} $RPM_BUILD_ROOT%{_var}/kerberos/krb5kdc/

# Where per-user keytabs live by default.
mkdir -p $RPM_BUILD_ROOT%{_var}/kerberos/krb5/user

# Default configuration file for everything.
mkdir -p $RPM_BUILD_ROOT/etc
install -pm 644 %{SOURCE5} $RPM_BUILD_ROOT/etc/krb5.conf

# Default include on this directory
mkdir -p $RPM_BUILD_ROOT/etc/krb5.conf.d
%if %{with crypto_policies}
ln -sv /etc/crypto-policies/back-ends/krb5.config $RPM_BUILD_ROOT/etc/krb5.conf.d/crypto-policies
%endif
install -pm 644 %{SOURCE50} $RPM_BUILD_ROOT/etc/krb5.conf.d

# Parent of configuration file for list of loadable GSS mechs ("mechs").  This
# location is not relative to sysconfdir, but is hard-coded in g_initialize.c.
mkdir -m 755 -p $RPM_BUILD_ROOT/etc/gss
# Parent of groups of configuration files for a list of loadable GSS mechs
# ("mechs").  This location is not relative to sysconfdir, and is also
# hard-coded in g_initialize.c.
mkdir -m 755 -p $RPM_BUILD_ROOT/etc/gss/mech.d

# If the default configuration needs to start specifying a default cache
# location, add it now, then fixup the timestamp so that it looks the same.
%if 0%{?configure_default_ccache_name}
export DEFCCNAME="%{configured_default_ccache_name}"
awk '{print}
     /^#    default_realm/{print "    default_ccache_name =", ENVIRON["DEFCCNAME"]}' \
     %{SOURCE5} > $RPM_BUILD_ROOT/etc/krb5.conf
touch -r %{SOURCE5} $RPM_BUILD_ROOT/etc/krb5.conf
grep default_ccache_name $RPM_BUILD_ROOT/etc/krb5.conf
%endif

# Server init scripts (krb5kdc,kadmind,kpropd) and their sysconfig files.
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
for unit in \
    %{SOURCE4}\
     %{SOURCE3} \
     %{SOURCE2} ; do
    # In the past, the init script was supposed to be named after the service
    # that the started daemon provided.  Changing their names is an
    # upgrade-time problem I'm in no hurry to deal with.
    install -pm 644 ${unit} $RPM_BUILD_ROOT%{_unitdir}
done
mkdir -p $RPM_BUILD_ROOT/%{_tmpfilesdir}
install -pm 644 %{SOURCE14} $RPM_BUILD_ROOT/%{_tmpfilesdir}/
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/run/krb5kdc

mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
for sysconfig in %{SOURCE8} %{SOURCE9} %{SOURCE10} ; do
    install -pm 644 ${sysconfig} \
            $RPM_BUILD_ROOT/etc/sysconfig/`basename ${sysconfig} .sysconfig`
done

# logrotate configuration files
mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d/
for logrotate in \
    %{SOURCE12} \
     %{SOURCE13} ; do
    install -pm 644 ${logrotate} \
            $RPM_BUILD_ROOT/etc/logrotate.d/`basename ${logrotate} .logrotate`
done

# PAM configuration files.
mkdir -p $RPM_BUILD_ROOT/etc/pam.d/
for pam in %{SOURCE11} ; do
    install -pm 644 ${pam} \
            $RPM_BUILD_ROOT/etc/pam.d/`basename ${pam} .pamd`
done

# Plug-in directories.
install -pdm 755 $RPM_BUILD_ROOT/%{_libdir}/krb5/plugins/preauth
install -pdm 755 $RPM_BUILD_ROOT/%{_libdir}/krb5/plugins/kdb
install -pdm 755 $RPM_BUILD_ROOT/%{_libdir}/krb5/plugins/authdata

# The rest of the binaries, headers, libraries, and docs.
%make_install -C src EXAMPLEDIR=%{libsdocdir}/examples

# Munge krb5-config yet again.  This is totally wrong for 64-bit, but chunks
# of the buildconf patch already conspire to strip out /usr/<anything> from the
# list of link flags, and it helps prevent file conflicts on multilib systems.
sed -r -i -e 's|^libdir=/usr/lib(64)?$|libdir=/usr/lib|g' $RPM_BUILD_ROOT%{_bindir}/krb5-config

# Workaround krb5-config reading too much from LDFLAGS.
# https://bugzilla.redhat.com/show_bug.cgi?id=1997021
# https://bugzilla.redhat.com/show_bug.cgi?id=2048909
sed -i -r -e 's/^(LDFLAGS=).*/\1/' $RPM_BUILD_ROOT%{_bindir}/krb5-config

# Install processed man pages.
%if %{with docs}
for section in 1 5 8 ; do
    install -m 644 build-man/*.${section} \
            $RPM_BUILD_ROOT/%{_mandir}/man${section}/
done
%endif

# I'm tired of warnings about these not having man pages
rm -- "$RPM_BUILD_ROOT/%{_sbindir}/krb5-send-pr"
rm -- "$RPM_BUILD_ROOT/%{_sbindir}/sim_server"
rm -- "$RPM_BUILD_ROOT/%{_sbindir}/gss-server"
rm -- "$RPM_BUILD_ROOT/%{_sbindir}/uuserver"
rm -- "$RPM_BUILD_ROOT/%{_bindir}/sim_client"
rm -- "$RPM_BUILD_ROOT/%{_bindir}/gss-client"
rm -- "$RPM_BUILD_ROOT/%{_bindir}/uuclient"

# These files are already packaged elsewhere
%if %{with docs}
rm -- "$RPM_BUILD_ROOT/%{_docdir}/krb5-libs/examples/kdc.conf"
rm -- "$RPM_BUILD_ROOT/%{_docdir}/krb5-libs/examples/krb5.conf"
rm -- "$RPM_BUILD_ROOT/%{_docdir}/krb5-libs/examples/services.append"
%endif

# This is only needed for tests
rm -- "$RPM_BUILD_ROOT/%{_libdir}/krb5/plugins/preauth/test.so"

%find_lang %{gettext_domain}

%ldconfig_scriptlets libs

%ldconfig_scriptlets server-ldap

%post server
%systemd_post krb5kdc.service kadmin.service kprop.service
# assert sanity.  A cleaner solution probably exists but it is opaque
/bin/systemctl daemon-reload
exit 0

%preun server
%systemd_preun krb5kdc.service kadmin.service kprop.service
exit 0

%postun server
%systemd_postun_with_restart krb5kdc.service kadmin.service kprop.service
exit 0

%ldconfig_scriptlets -n libkadm5

%files workstation
%doc src/config-files/services.append
%doc src/config-files/krb5.conf
%if %{with docs}
%doc build-html/*
%endif
%attr(0755,root,root) %doc src/config-files/convert-config-files

# Clients of the KDC, including tools you're likely to need if you're running
# app servers other than those built from this source package.
%{_bindir}/kdestroy
%{_mandir}/man1/kdestroy.1*
%{_bindir}/kinit
%{_mandir}/man1/kinit.1*
%{_bindir}/klist
%{_mandir}/man1/klist.1*
%{_bindir}/kpasswd
%{_mandir}/man1/kpasswd.1*
%{_bindir}/kswitch
%{_mandir}/man1/kswitch.1*

%{_bindir}/kvno
%{_mandir}/man1/kvno.1*
%{_bindir}/kadmin
%{_mandir}/man1/kadmin.1*
%{_bindir}/k5srvutil
%{_mandir}/man1/k5srvutil.1*
%{_bindir}/ktutil
%{_mandir}/man1/ktutil.1*

# Doesn't really fit anywhere else.
%attr(4755,root,root) %{_bindir}/ksu
%{_mandir}/man1/ksu.1*
%config(noreplace) /etc/pam.d/ksu

%files server
%docdir %{_mandir}
%doc src/config-files/kdc.conf
%{_unitdir}/krb5kdc.service
%{_unitdir}/kadmin.service
%{_unitdir}/kprop.service
%{_tmpfilesdir}/krb5-krb5kdc.conf
%dir %{_localstatedir}/run/krb5kdc
%config(noreplace) /etc/sysconfig/krb5kdc
%config(noreplace) /etc/sysconfig/kadmin
%config(noreplace) /etc/sysconfig/kprop
%config(noreplace) /etc/logrotate.d/krb5kdc
%config(noreplace) /etc/logrotate.d/kadmind

%dir %{_var}/kerberos
%dir %{_var}/kerberos/krb5kdc
%config(noreplace) %{_var}/kerberos/krb5kdc/kdc.conf
%config(noreplace) %{_var}/kerberos/krb5kdc/kadm5.acl

%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/kdb
%dir %{_libdir}/krb5/plugins/preauth
%dir %{_libdir}/krb5/plugins/authdata
%{_libdir}/krb5/plugins/preauth/otp.so
%{_libdir}/krb5/plugins/kdb/db2.so
%{_libdir}/krb5/plugins/kdb/klmdb.so

# KDC binaries and configuration.
%{_mandir}/man5/kadm5.acl.5*
%{_mandir}/man5/kdc.conf.5*
%{_sbindir}/kadmin.local
%{_mandir}/man8/kadmin.local.8*
%{_sbindir}/kadmind
%{_mandir}/man8/kadmind.8*
%{_sbindir}/kdb5_util
%{_mandir}/man8/kdb5_util.8*
%{_sbindir}/kprop
%{_mandir}/man8/kprop.8*
%{_sbindir}/kpropd
%{_mandir}/man8/kpropd.8*
%{_sbindir}/kproplog
%{_mandir}/man8/kproplog.8*
%{_sbindir}/krb5kdc
%{_mandir}/man8/krb5kdc.8*

# This is here for people who want to test their server.  It was formerly also
# included in -devel.
%{_bindir}/sclient
%{_mandir}/man1/sclient.1*
%{_sbindir}/sserver
%{_mandir}/man8/sserver.8*

%files server-ldap
%docdir %{_mandir}
%doc src/plugins/kdb/ldap/libkdb_ldap/kerberos.ldif
%doc src/plugins/kdb/ldap/libkdb_ldap/kerberos.schema
%doc 60kerberos.ldif
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/kdb
%{_libdir}/krb5/plugins/kdb/kldap.so
%{_libdir}/libkdb_ldap.so
%{_libdir}/libkdb_ldap.so.*
%{_mandir}/man8/kdb5_ldap_util.8.gz
%{_sbindir}/kdb5_ldap_util

%files libs -f %{gettext_domain}.lang
%doc README NOTICE
%{!?_licensedir:%global license %%doc}
%license LICENSE
%docdir %{_mandir}
# These are hard-coded, not-dependent-on-the-configure-script paths.
%dir /etc/gss
%dir /etc/gss/mech.d
%dir /etc/krb5.conf.d
%config(noreplace) /etc/krb5.conf
%if %{with crypto_policies}
%config(noreplace,missingok) /etc/krb5.conf.d/crypto-policies
%endif
/%{_sysconfdir}/krb5.conf.d/krb5-xs.conf
/%{_mandir}/man5/.k5identity.5*
/%{_mandir}/man5/.k5login.5*
/%{_mandir}/man5/k5identity.5*
/%{_mandir}/man5/k5login.5*
/%{_mandir}/man5/krb5.conf.5*
/%{_mandir}/man7/kerberos.7*
%{_libdir}/libgssapi_krb5.so.*
%{_libdir}/libgssrpc.so.*
%{_libdir}/libk5crypto.so.*
%{_libdir}/libkdb5.so.*
%{_libdir}/libkrad.so.*
%{_libdir}/libkrb5.so.*
%{_libdir}/libkrb5support.so.*
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/*
%{_libdir}/krb5/plugins/tls/k5tls.so
%{_libdir}/krb5/plugins/preauth/spake.so
%dir %{_var}/kerberos
%dir %{_var}/kerberos/krb5
%dir %{_var}/kerberos/krb5/user

%files pkinit
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/preauth
%{_libdir}/krb5/plugins/preauth/pkinit.so

%files devel
%docdir %{_mandir}

%{_includedir}/*
%{_libdir}/libgssapi_krb5.so
%{_libdir}/libgssrpc.so
%{_libdir}/libk5crypto.so
%{_libdir}/libkdb5.so
%{_libdir}/libkrad.so
%{_libdir}/libkrb5.so
%{_libdir}/libkrb5support.so
%{_libdir}/pkgconfig/*

%{_bindir}/krb5-config
%{_mandir}/man1/krb5-config.1*

%files -n libkadm5
%{_libdir}/libkadm5clnt.so
%{_libdir}/libkadm5clnt_mit.so
%{_libdir}/libkadm5srv.so
%{_libdir}/libkadm5srv_mit.so
%{_libdir}/libkadm5clnt_mit.so.*
%{_libdir}/libkadm5srv_mit.so.*

%changelog
* Tue Jul 07 2026 Philippe Coval <philippe.coval@vates.tech> - 1.21.3-4.1
- Rebuild with openssl-3
- *** Upstream changelog ***
  * Tue Nov 11 2025 Lin Liu <Lin.Liu01@cloud.com> - 1.21.3-4
  - CP-310102: Support build on XS8

  * Mon Jun 30 2025 Deli Zhang <deli.zhang@cloud.com> 1.21.3-3
  - CA-413120: Disable _kerberos-master SRV query for AD

  * Fri Apr 11 2025 Lin Liu <Lin.Liu01@cloud.com> - 1.21.3-2
  - CA-408551: XSI-1834: Disable dns_uri_lookup by default

  * Wed Jan 15 2025 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.21.3-1
  - CP-53144: Update to 1.21.3
  - CP-53144: Drop remnants of test package

  * Tue Nov 12 2024 Lin Liu <Lin.Liu01@cloud.com> - 1.21-3
  - CP-50489: Remove selinux

  * Tue Sep 24 2024 AshwinH <ashwin.h@cloud.com> - 1.21-2
  - CP-50735: Removed legacy Buildrequires words

  * Mon Sep 18 2023 Fei Su <fei.su@citrix.com> - 1.21-1
  - First imported release

* Tue Feb 10 2026 Philippe Coval <philippe.coval@vates.tech> - 1.15.1-22.1
- Skip keyring tests if keyring blocked by seccomp
- Add explicit dependency to gcc
- Make build dependency to latex optionnal
- Rebuild with openssl-3

* Wed Jul 16 2025 Deli Zhang <deli.zhang@cloud.com> 1.15.1-22
- CA-413120: Disable _kerberos-master SRV query for AD

* Tue Mar 25 2025 Lin Liu <Lin.Liu01@cloud.com> - 1.15.1-21
- CA-408551: XSI-1834: Disable dns_uri_lookup by default

* Fri Aug 23 2024 Deli Zhang <deli.zhang@citrix.com> - 1.15.1-20
- First imported release

