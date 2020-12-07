# Convolutional_Neural_Network

## Application level Configurations

### Creating a self signed certificate

- openssl req -newkey rsa:4096 -x509 -sha256 -days 3650 -nodes -out example.crt -keyout example.key

### Starting development server with https

- HTTPS=true SSL_CRT_FILE=./cert/cvapp.crt SSL_KEY_FILE=./cert/cvapp.key npm start

### Setting up Tomcat with https

```
If you want to generate an SSL cert for development purposes for use with tomcat, you can do it using this one liner (requires JDK on your machine, so this doesnt use openssl).

keytool -genkey -keyalg RSA -noprompt -alias tomcat -dname "CN=localhost, OU=NA, O=NA, L=NA, S=NA, C=NA" -keystore keystore.jks -validity 9999 -storepass changeme -keypass changeme


This generates a keystore.jks file with a password of changeme using a keyAlias of tomcat that's valid for 9999 days for localhost

In your tomcat/conf/server.xml, you'd need to specify it like so in your <Connector>

    keyAlias="tomcat"
    keystoreFile="/path/to/my/keystore.jks"
    keystorePass="changeme"

Since Tomcat 8

According to the documentation:

NIO and NIO2 SSL configuration attributes have been deprecated in favor of the default SSLHostConfig

This means the values above should now be put as attributes of connector/SSLHostConfig/Certificate with these names:

    certificateKeyAlias="tomcat"
    certificateKeystoreFile="/path/to/my/keystore.jks"
    certificateKeystorePassword="changeme"
```

### open port

- sudo ufw allow 8443

### Update server.xml with port 8443 tag using sed

    https_tag='<Connector\tport="8443"\tprotocol="org.apache.coyote.http11.Http11NioProtocol"\tmaxThreads="150"\tSSLEnabled="true">\n<SSLHostConfig>\n<Certificate\tcertificateKeyAlias="tomcat"\tcertificateKeystoreFile="conf/keystore.jks"\tcertificateKeystorePassword="changeme"\ttype="RSA"/>\n</SSLHostConfig>\n</Connector>'


    sed -i '\/<Service name="Catalina">/a '$https_tag /opt/tomcat/conf/server.xml

- Some info like keystore location can be updated either by variable name or location info
- spaces are replaced by '\t' and new lines are replaced by '\n'
