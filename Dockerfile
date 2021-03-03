#######################
# Choose an OS or runtime environment image that fits the needs of your experiment e.g.
#FROM debian:jessie
#Or:
FROM python:3.8-slim
#######################
WORKDIR /docker

COPY . /docker
#Define input/output directories
VOLUME /input
VOLUME /output

CMD [ "python", "test-docker/main.py" ]

#/datasets"
#VOLUME "/output/tables_and_plots"

# pour docker-test
#ADD
#RUN
#ENTRYPOINT ./run-test.sh

#Add and set entrypoint 
#ADD run.sh /run.sh
#RUN chmod u+x /run.sh
#ENTRYPOINT /run.sh

#######################
# Customization start #
#######################

#Add any custom dependencies and/or scripts here

#######################
# Customization end   #
#######################
