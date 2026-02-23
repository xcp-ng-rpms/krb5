%bcond_with docs

%global package_speccommit cc9fd54eb74c0e9d25a69bc45ecf7f6df1cd8de6
%global usver 1.15.1
%global xsver 22
%global xsrel %{xsver}%{?xscount}%{?xshash}

%global WITH_DIRSRV 1

# Set this so that find-lang.sh will recognize the .po files.
%global gettext_domain mit-krb5

# Guess where the -libs subpackage's docs are going to go.
%define libsdocdir %{?_pkgdocdir:%(echo %{_pkgdocdir} | sed -e s,krb5,krb5-libs,g)}%{!?_pkgdocdir:%{_docdir}/%{name}-libs-%{version}}

# Figure out where the default ccache lives and how we set it.
%global configured_default_ccache_name KEYRING:persistent:%%{uid}

Summary: The Kerberos network authentication system
Name: krb5
Version: 1.15.1
Release: %{?xsrel}.1%{?dist}

# - Maybe we should explode from the now-available-to-everybody tarball instead?
# http://web.mit.edu/kerberos/dist/krb5/1.13/krb5-1.13.2-signed.tar
# - The sources below are stored in a lookaside cache. Upload with
# $ rhpkg upload krb5-1.13.2.tar.gz krb5-1.13.2.tar.gz.asc # (and don't
# remove, otherwise you can't go back or branch from a previous point)
Source0: krb5-1.15.1.tar.gz
Source2: kprop.service
Source4: kadmin.service
Source5: krb5kdc.service
Source6: krb5.conf
Source7: _kpropd
Source8: _kadmind
Source10: kdc.conf
Source11: kadm5.acl
Source19: krb5kdc.sysconfig
Source20: kadmin.sysconfig
Source21: kprop.sysconfig
Source29: ksu.pamd
Source31: kerberos-adm.portreserve
Source32: krb5_prop.portreserve
Source33: krb5kdc.logrotate
Source34: kadmind.logrotate
Source36: kpropd.init
Source37: kadmind.init
Source38: krb5kdc.init
Source39: krb5-krb5kdc.conf
Source50: krb5-xs.conf
Patch0: krb5-1.12.1-pam.patch
Patch1: krb5-1.15-beta1-selinux-label.patch
Patch2: krb5-1.12-ksu-path.patch
Patch3: krb5-1.12-ktany.patch
Patch4: krb5-1.15-beta1-buildconf.patch
Patch5: krb5-1.3.1-dns.patch
Patch6: krb5-1.12-api.patch
Patch7: krb5-1.13-dirsrv-accountlock.patch
Patch8: krb5-1.9-debuginfo.patch
Patch9: krb5-kvno-230379.patch
Patch10: krb5-1.11-run_user_0.patch
Patch11: krb5-1.11-kpasswdtest.patch
Patch12: Improve-PKINIT-UPN-SAN-matching.patch
Patch13: Deindent-crypto_retrieve_X509_sans.patch
Patch14: Add-certauth-pluggable-interface.patch
Patch15: Correct-error-handling-bug-in-prior-commit.patch
Patch16: Add-the-client_name-kdcpreauth-callback.patch
Patch17: Use-the-canonical-client-principal-name-for-OTP.patch
Patch18: Remove-incomplete-PKINIT-OCSP-support.patch
Patch19: Add-support-to-query-the-SSF-of-a-GSS-context.patch
Patch20: Add-k5test-expected_msg-expected_trace.patch
Patch21: Add-PKINIT-UPN-tests-to-t_pkinit.py.patch
Patch22: Add-test-cert-generation-to-make-certs.sh.patch
Patch23: Fix-make-certs.sh-for-OpenSSL-1.1.patch
Patch24: Allow-clock-skew-in-krb5-gss_context_time.patch
Patch25: Fix-in_clock_skew-and-use-it-in-AS-client-code.patch
Patch26: Add-timestamp-helper-functions.patch
Patch27: Make-timestamp-manipulations-y2038-safe.patch
Patch28: Add-timestamp-tests.patch
Patch29: Add-y2038-documentation.patch
Patch30: Fix-more-time-manipulations-for-y2038.patch
Patch31: Use-krb5_timestamp-where-appropriate.patch
Patch32: Add-KDC-policy-pluggable-interface.patch
Patch33: Fix-bugs-in-kdcpolicy-commit.patch
Patch34: Prevent-KDC-unset-status-assertion-failures.patch
Patch35: Convert-some-pkiDebug-messages-to-TRACE-macros.patch
Patch36: Fix-certauth-built-in-module-returns.patch
Patch37: Add-test-cert-with-no-extensions.patch
Patch38: Expose-context-errors-in-pkinit_server_plugin_init.patch
Patch39: Limit-ticket-lifetime-to-2-31-1-seconds.patch
Patch40: Disable-_kerberos-master-SRV-query-for-AD.patch
Patch41: Skip-keyring-tests-if-keyring-blocked-by-seccomp.patch

BuildRequires: gcc

BuildRequires: cmake xz
# Carry this locally until it's available in a packaged form.
Source100: nss_wrapper-0.0-20140204195100.git3d58327.tar.xz
Source101: noport.c
Source102: socket_wrapper-0.0-20140204194748.gitf3b2ece.tar.xz

License: MIT
URL: http://web.mit.edu/kerberos/www/
Group: System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: autoconf, bison, flex, gawk, gettext, pkgconfig, sed
BuildRequires: libcom_err-devel, libedit-devel, libss-devel
BuildRequires: gzip, ncurses-devel

%if %{with docs}
BuildRequires: texlive-pdftex

# Taken from \usepackage directives produced by sphinx:
BuildRequires: tex(babel.sty)
BuildRequires: tex(bookmark.sty)
BuildRequires: tex(fancybox.sty)
BuildRequires: tex(fncychap.sty)
BuildRequires: tex(fontenc.sty)
BuildRequires: tex(framed.sty)
BuildRequires: tex(hyperref.sty)
BuildRequires: tex(ifthen.sty)
BuildRequires: tex(inputenc.sty)
BuildRequires: tex(longtable.sty)
BuildRequires: tex(multirow.sty)
BuildRequires: tex(times.sty)
BuildRequires: tex(titlesec.sty)
BuildRequires: tex(threeparttable.sty)
BuildRequires: tex(wrapfig.sty)
BuildRequires: tex(report.cls)

# Typical fonts, and the commands which we need to have present.
BuildRequires: texlive, texlive-latex, texlive-texmf-fonts
BuildRequires: /usr/bin/pdflatex /usr/bin/makeindex
%endif

BuildRequires: keyutils, keyutils-libs-devel >= 1.5.8
BuildRequires: libselinux-devel
BuildRequires: pam-devel
BuildRequires: systemd-units
# For the test framework.
BuildRequires: perl, dejagnu, tcl-devel
BuildRequires: net-tools, rpcbind
BuildRequires: hostname
BuildRequires: iproute

# someday...
%if 0%{?fedora} >= 9
BuildRequires: python-pyrad
%endif
%if 0%{?fedora} >= 8
%ifarch %{ix86} x86_64
BuildRequires: yasm
%endif
%endif

BuildRequires: openldap-devel
BuildRequires: openssl-devel >= 0.9.8
BuildRequires: libverto-devel

%description
Kerberos V5 is a trusted-third-party network authentication system,
which can improve your network's security by eliminating the insecure
practice of sending passwords over the network in unencrypted form.

%package devel
Summary: Development files needed to compile Kerberos 5 programs
Group: Development/Libraries
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: libkadm5%{?_isa} = %{version}-%{release}
Requires: libcom_err-devel
Requires: keyutils-libs-devel, libselinux-devel
Requires: libverto-devel

%description devel
Kerberos is a network authentication system. The krb5-devel package
contains the header files and libraries needed for compiling Kerberos
5 programs. If you want to develop Kerberos-aware programs, you need
to install this package.

%package libs
Summary: The non-admin shared libraries used by Kerberos 5
Group: System Environment/Libraries
Requires: coreutils, gawk, grep, sed
Requires: keyutils-libs >= 1.5.8

%description libs
Kerberos is a network authentication system. The krb5-libs package
contains the shared libraries needed by Kerberos 5. If you are using
Kerberos, you need to install this package.

%package server
Group: System Environment/Daemons
Summary: The KDC and related programs for Kerberos 5
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
# we drop files in its directory, but we don't want to own that directory
Requires: logrotate
# we specify /usr/share/dict/words as the default dict_file in kdc.conf
Requires: /usr/share/dict/words
# for run-time, and for parts of the test suite
BuildRequires: libverto-module-base
Requires: libverto-module-base
Requires: libkadm5%{?_isa} = %{version}-%{release}

%description server
Kerberos is a network authentication system. The krb5-server package
contains the programs that must be installed on a Kerberos 5 key
distribution center (KDC).  If you are installing a Kerberos 5 KDC,
you need to install this package (in other words, most people should
NOT install this package).

%package server-ldap
Group: System Environment/Daemons
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
Group: System Environment/Base
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: libkadm5%{?_isa} = %{version}-%{release}
# mktemp is used by krb5-send-pr
Requires: coreutils

%description workstation
Kerberos is a network authentication system. The krb5-workstation
package contains the basic Kerberos programs (kinit, klist, kdestroy,
kpasswd). If your network uses Kerberos, this package should be
installed on every workstation.

%package pkinit
Summary: The PKINIT module for Kerberos 5
Group: System Environment/Libraries
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
Group: System Environment/Base
Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description -n libkadm5
Kerberos is a network authentication system. The libkadm5 package
contains the libkadm5clnt and libkadm5serv shared objects, for use
ONLY by kerberos itself. Do not depend on this package.

%prep
# Apply run_user_0 when the hard-wired or configured default location is
# DIR:/run/user/%%{uid}/krb5cc.
%setup -q -a 100 -a 102
%autopatch -p1

ln NOTICE LICENSE

chmod u+x src/util/paste-kdcproxy.py
# Take the execute bit off of documentation.
chmod -x doc/ccapi/*.html

# Generate an FDS-compatible LDIF file.
inldif=src/plugins/kdb/ldap/libkdb_ldap/kerberos.ldif
cat > '60kerberos.ldif' << EOF
# This is a variation on kerberos.ldif which 389 Directory Server will like.
dn: cn=schema
EOF
grep -E -iv '(^$|^dn:|^changetype:|^add:)' $inldif | \
sed -r 's,^		,                ,g' | \
sed -r 's,^	,        ,g' >> 60kerberos.ldif
touch -r $inldif 60kerberos.ldif

# Rebuild the configure scripts.
pushd src
autoreconf -fiv
popd

# Create build spaces for the test wrappers.
mkdir -p nss_wrapper/build
mkdir -p socket_wrapper/build

# Mess with some of the default ports that we use for testing, so that multiple
# builds going on the same host don't step on each other.
cfg="src/kadmin/testing/proto/kdc.conf.proto \
     src/kadmin/testing/proto/krb5.conf.proto \
     src/lib/kadm5/unit-test/api.current/init-v2.exp \
     src/util/k5test.py"
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

%build
# Go ahead and supply tcl info, because configure doesn't know how to find it.
source %{_libdir}/tclConfig.sh
pushd src

# Set this so that configure will have a value even if the current version of
# autoconf doesn't set one.
runstatedir=%{_localstatedir}/run; export runstatedir
# Work out the CFLAGS and CPPFLAGS which we intend to use.
INCLUDES=-I%{_includedir}/et
CFLAGS="`echo $RPM_OPT_FLAGS $DEFINES $INCLUDES -fPIC -fno-strict-aliasing -fstack-protector-all`"
CPPFLAGS="`echo $DEFINES $INCLUDES`"
%configure \
	CC="%{__cc}" \
	CFLAGS="$CFLAGS" \
	CPPFLAGS="$CPPFLAGS" \
%if 0%{?fedora} >= 7 || 0%{?rhel} >= 6
	SS_LIB="-lss" \
%else
	SS_LIB="-lss -lncurses" \
%endif
	--enable-shared \
	--localstatedir=%{_var}/kerberos \
	--disable-rpath \
	--without-krb5-config \
	--with-system-et \
	--with-system-ss \
	--with-netlib=-lresolv \
	--with-tcl \
	--enable-dns-for-realm \
	--with-ldap \
%if %{WITH_DIRSRV}
	--with-dirsrv-account-locking \
%endif
	--enable-pkinit \
	--with-pkinit-crypto-impl=openssl \
	--with-tls-impl=openssl \
	--with-system-verto \
	--with-pam \
	--with-selinux \
        --with-prng-alg=os
# Now build it.
make
popd

# Sanity check the KDC_RUN_DIR.
configured_kdcrundir=`grep KDC_RUN_DIR src/include/osconf.h | awk '{print $NF}'`
configured_kdcrundir=`eval echo $configured_kdcrundir`
if test "$configured_kdcrundir" != %{_localstatedir}/run/krb5kdc ; then
	exit 1
fi

# Build the test wrappers.
pushd nss_wrapper/build
cmake ..
make
popd
pushd socket_wrapper/build
cmake ..
make
popd

# We need to cut off any access to locally-running nameservers, too.
%{__cc} -fPIC -shared -o noport.so -Wall -Wextra %{SOURCE101}

%check
# Alright, this much is still a work in progress.
%if %{?__isa_bits:%{__isa_bits}}%{!?__isa_bits:32} == 64
if hostname | grep -q build ; then
	sleep 600
fi
%endif

# Set things up to use the test wrappers.
NSS_WRAPPER_HOSTNAME=test.example.com ; export NSS_WRAPPER_HOSTNAME
NSS_WRAPPER_HOSTS="`pwd`/nss_wrapper/fakehosts" ; export NSS_WRAPPER_HOSTS
echo 127.0.0.1 $NSS_WRAPPER_HOSTNAME $NSS_WRAPPER_HOSTNAME localhost localhost >"$NSS_WRAPPER_HOSTS"
NOPORT=53,111; export NOPORT
SOCKET_WRAPPER_DIR=`pwd`/sockets; mkdir -p $SOCKET_WRAPPER_DIR; export SOCKET_WRAPPER_DIR
LD_PRELOAD=`pwd`/noport.so:`pwd`/nss_wrapper/build/src/libnss_wrapper.so:`pwd`/socket_wrapper/build/src/libsocket_wrapper.so ; export LD_PRELOAD

# Run the test suite. We can't actually run the whole thing in the build
# system, but we can at least run more than we used to.  The build system may
# give us a revoked session keyring, so run affected tests with a new one.
make -C src runenv.py
: make -C src check TMPDIR=%{_tmppath}
keyctl session - make -C src/lib check TMPDIR=%{_tmppath} OFFLINE=yes
make -C src/kdc check TMPDIR=%{_tmppath}
keyctl session - make -C src/appl check TMPDIR=%{_tmppath}
make -C src/clients check TMPDIR=%{_tmppath}
keyctl session - make -C src/util check TMPDIR=%{_tmppath}

%install
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf -- $RPM_BUILD_ROOT

# Sample KDC config files (bundled kdc.conf and kadm5.acl).
mkdir -p $RPM_BUILD_ROOT%{_var}/kerberos/krb5kdc
install -pm 600 %{SOURCE10} $RPM_BUILD_ROOT%{_var}/kerberos/krb5kdc/
install -pm 600 %{SOURCE11} $RPM_BUILD_ROOT%{_var}/kerberos/krb5kdc/

# Where per-user keytabs live by default.
mkdir -p $RPM_BUILD_ROOT%{_var}/kerberos/krb5/user

# Default configuration file for everything.
mkdir -p $RPM_BUILD_ROOT/etc
install -pm 644 %{SOURCE6} $RPM_BUILD_ROOT/etc/krb5.conf

# Default include on this directory
mkdir -p $RPM_BUILD_ROOT/etc/krb5.conf.d
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
DEFCCNAME="%{configured_default_ccache_name}"; export DEFCCNAME
awk '{print}
     /^# default_realm/{print " default_ccache_name =", ENVIRON["DEFCCNAME"]}' \
     %{SOURCE6} > $RPM_BUILD_ROOT/etc/krb5.conf
touch -r %{SOURCE6} $RPM_BUILD_ROOT/etc/krb5.conf
grep default_ccache_name $RPM_BUILD_ROOT/etc/krb5.conf

# Server init scripts (krb5kdc,kadmind,kpropd) and their sysconfig files.
mkdir -p $RPM_BUILD_ROOT%{_unitdir}
for unit in \
	%{SOURCE5}\
	%{SOURCE4} \
	%{SOURCE2} ; do
	# In the past, the init script was supposed to be named after the
	# service that the started daemon provided.  Changing their names
	# is an upgrade-time problem I'm in no hurry to deal with.
	install -pm 644 ${unit} $RPM_BUILD_ROOT%{_unitdir}
done
mkdir -p $RPM_BUILD_ROOT%{_sbindir}
for wrapper in \
	%{SOURCE7} \
	%{SOURCE8} ; do
	install -pm 755 ${wrapper} $RPM_BUILD_ROOT%{_sbindir}/
done
mkdir -p $RPM_BUILD_ROOT/%{_tmpfilesdir}
install -pm 644 %{SOURCE39} $RPM_BUILD_ROOT/%{_tmpfilesdir}/
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/run/krb5kdc

mkdir -p $RPM_BUILD_ROOT/etc/sysconfig
for sysconfig in \
	%{SOURCE19}\
	%{SOURCE20}\
	%{SOURCE21} ; do
	install -pm 644 ${sysconfig} \
	$RPM_BUILD_ROOT/etc/sysconfig/`basename ${sysconfig} .sysconfig`
done

# logrotate configuration files
mkdir -p $RPM_BUILD_ROOT/etc/logrotate.d/
for logrotate in \
	%{SOURCE33} \
	%{SOURCE34} ; do
	install -pm 644 ${logrotate} \
	$RPM_BUILD_ROOT/etc/logrotate.d/`basename ${logrotate} .logrotate`
done

# PAM configuration files.
mkdir -p $RPM_BUILD_ROOT/etc/pam.d/
for pam in \
	%{SOURCE29} ; do
	install -pm 644 ${pam} \
	$RPM_BUILD_ROOT/etc/pam.d/`basename ${pam} .pamd`
done

# Plug-in directories.
install -pdm 755 $RPM_BUILD_ROOT/%{_libdir}/krb5/plugins/preauth
install -pdm 755 $RPM_BUILD_ROOT/%{_libdir}/krb5/plugins/kdb
install -pdm 755 $RPM_BUILD_ROOT/%{_libdir}/krb5/plugins/authdata

# The rest of the binaries, headers, libraries, and docs.
make -C src DESTDIR=$RPM_BUILD_ROOT EXAMPLEDIR=%{libsdocdir}/examples install

# Munge krb5-config yet again.  This is totally wrong for 64-bit, but chunks
# of the buildconf patch already conspire to strip out /usr/<anything> from the
# list of link flags, and it helps prevent file conflicts on multilib systems.
sed -r -i -e 's|^libdir=/usr/lib(64)?$|libdir=/usr/lib|g' $RPM_BUILD_ROOT%{_bindir}/krb5-config

# FIXME: Temporay workaround for RH bug #1204646 ("krb5-config
# returns wrong -specs path") so that development of krb5
# dependicies gets unstuck.
sed -r -i -e "s/-specs=\/.+?\/redhat-hardened-ld//g" $RPM_BUILD_ROOT%{_bindir}/krb5-config

if [[ "$(< $RPM_BUILD_ROOT%{_bindir}/krb5-config )" == *redhat-hardened-ld* ]] ; then
       printf '# redhat-hardened-ld for krb5-config failed' 1>&2
       exit 1
fi

# This script just tells you to send bug reports to krb5-bugs@mit.edu, but
# since we don't have a man page for it, just drop it.
rm -- $RPM_BUILD_ROOT/%{_sbindir}/krb5-send-pr

# These files are already packaged elsewhere
rm -f -- "$RPM_BUILD_ROOT/%{_docdir}/krb5-libs/examples/kdc.conf"
rm -f -- "$RPM_BUILD_ROOT/%{_docdir}/krb5-libs/examples/krb5.conf"
rm -f -- "$RPM_BUILD_ROOT/%{_docdir}/krb5-libs/examples/services.append"

# This is only needed for tests
rm -- "$RPM_BUILD_ROOT/%{_libdir}/krb5/plugins/preauth/test.so"

%find_lang %{gettext_domain}

%clean
[ "$RPM_BUILD_ROOT" != '/' ] && rm -rf -- $RPM_BUILD_ROOT

%post libs -p /sbin/ldconfig

%triggerun libs -- krb5-libs < 1.15.1-13
if ! grep -q 'includedir /etc/krb5.conf.d' /etc/krb5.conf ; then
    sed -i '1i # Other applications require this directory to perform krb5 configuration.\nincludedir /etc/krb5.conf.d/\n' /etc/krb5.conf
fi

%postun libs -p /sbin/ldconfig

%post server-ldap -p /sbin/ldconfig

%postun server-ldap -p /sbin/ldconfig

%post server
# assert sanity.  A cleaner solution probably exists but it is opaque.
/bin/systemctl daemon-reload
exit 0

%preun server
if [ "$1" -eq "0" ] ; then
	/bin/systemctl --no-reload disable krb5kdc.service > /dev/null 2>&1 || :
	/bin/systemctl --no-reload disable kadmin.service > /dev/null 2>&1 || :
	/bin/systemctl --no-reload disable kprop.service > /dev/null 2>&1 || :
	/bin/systemctl stop krb5kdc.service > /dev/null 2>&1 || :
	/bin/systemctl stop kadmin.service > /dev/null 2>&1 || :
	/bin/systemctl stop kprop.service > /dev/null 2>&1 || :
fi
exit 0

%postun server
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ "$1" -ge 1 ] ; then
	/bin/systemctl try-restart krb5kdc.service >/dev/null 2>&1 || :
	/bin/systemctl try-restart kadmin.service >/dev/null 2>&1 || :
	/bin/systemctl try-restart kprop.service >/dev/null 2>&1 || :
fi
exit 0

%post -n libkadm5 -p /sbin/ldconfig

%postun -n libkadm5 -p /sbin/ldconfig

%files workstation
%defattr(-,root,root,-)
%doc src/config-files/services.append
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
%defattr(-,root,root,-)
%docdir %{_mandir}
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

# KDC binaries and configuration.
%{_mandir}/man5/kadm5.acl.5*
%{_mandir}/man5/kdc.conf.5*
%{_sbindir}/kadmin.local
%{_mandir}/man8/kadmin.local.8*
%{_sbindir}/kadmind
%{_sbindir}/_kadmind
%{_mandir}/man8/kadmind.8*
%{_sbindir}/kdb5_util
%{_mandir}/man8/kdb5_util.8*
%{_sbindir}/kprop
%{_mandir}/man8/kprop.8*
%{_sbindir}/kpropd
%{_sbindir}/_kpropd
%{_mandir}/man8/kpropd.8*
%{_sbindir}/kproplog
%{_mandir}/man8/kproplog.8*
%{_sbindir}/krb5kdc
%{_mandir}/man8/krb5kdc.8*

# This is here for people who want to test their server.  It was formerly also
# in -devel.
%{_bindir}/sclient
%{_mandir}/man1/sclient.1*
%{_sbindir}/sserver
%{_mandir}/man8/sserver.8*

%files server-ldap
%defattr(-,root,root,-)
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
%defattr(-,root,root,-)
%doc README NOTICE
%{!?_licensedir:%global license %%doc}
%license LICENSE
%docdir %{_mandir}
# These are hard-coded, not-dependent-on-the-configure-script paths.
%dir /etc/gss
%dir /etc/gss/mech.d
%dir /etc/krb5.conf.d
%config(noreplace) /etc/krb5.conf
/%{_sysconfdir}/krb5.conf.d/krb5-xs.conf
/%{_mandir}/man5/.k5identity.5*
/%{_mandir}/man5/.k5login.5*
/%{_mandir}/man5/k5identity.5*
/%{_mandir}/man5/k5login.5*
/%{_mandir}/man5/krb5.conf.5*
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
%dir %{_var}/kerberos
%dir %{_var}/kerberos/krb5
%dir %{_var}/kerberos/krb5/user

%files pkinit
%defattr(-,root,root,-)
%dir %{_libdir}/krb5
%dir %{_libdir}/krb5/plugins
%dir %{_libdir}/krb5/plugins/preauth
%{_libdir}/krb5/plugins/preauth/pkinit.so

%files devel
%defattr(-,root,root,-)
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

# Protocol test clients.
%{_bindir}/sim_client
%{_bindir}/gss-client
%{_bindir}/uuclient

# Protocol test servers.
%{_sbindir}/sim_server
%{_sbindir}/gss-server
%{_sbindir}/uuserver

%files -n libkadm5
%defattr(-,root,root,-)
%{_libdir}/libkadm5clnt.so
%{_libdir}/libkadm5clnt_mit.so
%{_libdir}/libkadm5srv.so
%{_libdir}/libkadm5srv_mit.so
%{_libdir}/libkadm5clnt_mit.so.*
%{_libdir}/libkadm5srv_mit.so.*

%changelog
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

