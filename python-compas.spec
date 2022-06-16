%global pypi_name compas
%global proj_name compas
%global pkg_names %{proj_name} compas_blender compas_ghpython compas_plotters compas_rhino

Name:           python-%{pypi_name}
Version:        1.15.1
Release:        1%{?dist}
Summary:        The COMPAS framework

License:        MIT
URL:            https://github.com/compas-dev/%{proj_name}
Source:         %{url}/archive/v%{version}/%{proj_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# Test dependencies:
BuildRequires: python3dist(pytest)

Suggests: python3-%{pypi_name}+extras

%global _description %{expand:
The COMPAS framework is an open-source, Python-based framework for computational
research and collaboration in architecture, engineering, digital fabrication and
construction.

The framework consists of a general-purpose core library, written in pure
Python, and a growing collection of extensions that provide easy access to
peer-reviewed research, state-of-the-art external libraries such as CGAL, libigl
and Triangle, and tools with specialized functionality for AEFC applications
such as Abaqus, ANSYS, SOFISTIK, ROS, etc.

COMPAS has dedicated packages for working with Rhino, Grasshopper, and Blender,
but it can be used in any environment that supports Python scripting. It is
available on PyPI and conda-forge and can be easily installed using popular
package managers on multiple platforms.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%pyproject_extras_subpkg -n python3-%{pypi_name} extras

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files %{pkg_names}

%check
# fix rpc tests
sed -i -e "s#python='python'#python='%{python3}'#" tests/compas/rpc/test_rpc.py

# test_compas_api_stubs requires sphinx-autogen and not relevant to the package
%pytest tests -k "not test_compas_api_stubs"

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/compas_rpc

%changelog
* Thu Jun 16 2022 Anton Tetov <anton@tetov.se> - 1.15.1-1
- Initial package.
