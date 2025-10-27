<h1 align="center"> HiveBox - DevOps End-to-End Hands-On Project </h1>

## Prerequisites
> [!IMPORTANT]
> You should have **Docker** installed in order to run this project.

## Usage
1. Clone this repository using `git` command:
  ```bash
  git clone https://github.com/SlyPex/devops-hands-on-project-hivebox.git
  ```
2. `cd` into the repository directory:
  ```
  cd devops-hands-on-project-hivebox
  ```
3. Build the docker image:
  ```bash
  docker build . -t hivebox:0.0.1
  ```
4. Run the project using:
  ```
  docker run --rm hivebox:0.0.1
  ```
5. You should see an output like this:
  ```
  Current Version : v0.0.1
  ```