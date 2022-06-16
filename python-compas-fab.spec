%global pypi_name compas-fab
%global proj_name compas_fab
%global pkg_names %{proj_name}

Name:           python-%{pypi_name}
Version:        0.25.0
Release:        1%{?dist}
Summary:        The COMPAS framework

License:        MIT
URL:            https://github.com/compas-dev/%{proj_name}
Source:         %{url}/archive/v%{version}/%{proj_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

# Test dependencies:
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-cov)

Suggests: python3-%{pypi_name}+extras

%global _description %{expand:
Robotic fabrication package for the COMPAS Framework that facilitates the
planning and execution of robotic fabrication processes. It provides interfaces
to existing software libraries and tools available in the field of robotics
(e.g. OMPL, ROS) and makes them accessible from within the parametric design
environment. The package builds upon COMPAS, an open-source Python-based
framework for collaboration and research in architecture, engineering and
digital fabrication.}

%description %_description

%package -n python3-%{pypi_name}
Summary: %{summary}

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

%pytest tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
* Thu Jun 16 2022 Anton Tetov <anton@tetov.se> - 0.25.0-1
- Initial package.
