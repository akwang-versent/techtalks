FROM alpine
RUN apk update && \
    apk add curl unzip vim sed 

ENV PACKAGE_SOURCE=https://d3n46h3syaq3jo.cloudfront.net/b68748f5594ce2e8defceb9afe4a1b8eb74fb364/2020-05-21_AMS_CLI.zip
ENV PACKAGE_TARGET=2020-05-21_AMS_CLI.zip

RUN curl ${PACKAGE_SOURCE} -o ${PACKAGE_TARGET} \
    && unzip ${PACKAGE_TARGET} \
    && cd "./2020-05-21_AMS_CLI/Linux and Mac/" \
    && chmod u+x ./AWSManagedServices_InstallCLI.sh \
    && sed -i 's/select yn in "Yes" "No"; do/yn="Yes"/' ./AWSManagedServices_InstallCLI.sh \
    && sed -i 's/break;;/;;/' ./AWSManagedServices_InstallCLI.sh \ 
    && sed -i 's/exit;;/;;/' ./AWSManagedServices_InstallCLI.sh \ 
    && sed -i 's/done//' ./AWSManagedServices_InstallCLI.sh \
    && sh ./AWSManagedServices_InstallCLI.sh

# ENTRYPOINT ["/bin/sh"]

# LINE BELOW IS FOR ALPINE TESTING
#    && sed -i 's/#!\/bin\/bash/#!\/bin\/sh/' ./AWSManagedServices_InstallCLI.sh \
