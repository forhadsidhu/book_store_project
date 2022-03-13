
container is like the apartment of buildings using part of piller and plumber and virtual Environment is like
full building using pillar plumbers

image is the blueprint or set of plans of the apartments and the container is the actual
fully-built building

Dockerfile:
         1. read from top-to-bottom when an image is created
         2.First instruction is FROM command which let us to import base image
         3. set up ENV
             ENV PYTHONUNBUFFERED 1        ensures our console output looks familiar and is not buffered
                                          by Docker, which we don’t want
               ENV PYTHONDONTWRITEBYTECODE 1    means Python will not try to write .pyc files which we
                                          also do not desire
                                          
         WORKDIR /code --> we will store our code,Docker will just assume we mean to execute all commands from this directory
         
         COPY Pipfile Pipfile.lock /code/  ->  dependencies,copy over both the Pipfile and
                                             Pipfile.lock files into a /code/ directory in Docker


         Pipfile.lock -> benefit is leads to a deterministic build. how many install get same result.
                         without that that will locks down the dependencies and their order, so if team install get
                          different results.
                          
                          -->RUN pip install pipenv  install software list in Pipfile.lock
                          -->  --system flag to ensure our packages are available throughout all of Docker for us
                          
                          
          COPY . /code/
                          
                          why need 2 copy one is env another this->reason is that images are created based on
                                    instructions top-down so we want things that change often–like our local code–to
                                                    be last
                                                    
          
          docker build . indicated the current directory where to execute the command
                                             
                                                  
          ocker-compose.yml ->     file to control how to run the container that will be built based upon our
                                     Dockerfile image      
                                     
                            version: '3.7' - just version of the docker
                            services: ->  services (or containers) we want to have running within our Docker host
                            web-> web name service
                            build: . -> specify how to build the container by saying, Look in the current directory
                             . for the Dockerfile
                             command: python /code/manage.py runserver 0.0.0.0:8000 ->within the container run the command to start up
                                the local server
                             volumes:
                                 - .:/code -> mount automatically syncs the Docker filesystem with our local
                                             computer’s filesystem,don’t have to rebuild the image each time
                                               we change a single file
                              ports to expose within Docker which will be 8000, which is the
                                Django default
                                
                                Containers are meant to be stateless which is why we use volumes to copy our code
                               over locally where it can be saved
                               
           docker-compose up -d                    
          Detached mode runs containers in the background40, which means we can use a single
              command line tab without needing a separate one open as well
           
         docker-compose exec [service]
               where we specify the name of the service
               docker-compose exec web python manage.py createsuperuser
               
               
         docker-compose up -d ->  rebuild our image and spin up two containers, one running PostgreSQL within db and
          the other our Django web server.
          
          
          docker-compose logs
          should always install package via docker
          
          docker-compose up -d --build -> force an image rebuild
          
           
   This means that the data doesn’t persist when the container is removed. Yes, you will lose all the cookies if you store them inside a container! Don’t do that.
   
    Volumes are the preferred way to persist data in Docker

They are easier to back up or migrate than bind mounts. They are manageable using either the CLI or the Docker API. They can be more safely shared among multiple containers. Volume drivers let you store volumes on remote hosts or cloud providers, to encrypt the contents of volumes, or to add other functionality. New volumes can have their content pre-populated by a container.
 Higher performance on Docker Desktop for windows and Mac
 
 
 Volumes are stored in a part of the host filesystem managed by Docker. The exact folder depends on the operating system. For example, on Linux, it's:

/var/lib/docker/volumes/




docker ps -a  #see the container list
 