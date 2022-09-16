/* @TODO replace with your variables
 * ensure all variables on this page match your project
 */

export const environment = {
  production: false,
  apiServerUrl: 'http://localhost:8080', // the running FLASK api server url
  auth0: {
    url: 'auticon-conjohn712.us', // the auth0 domain prefix
    audience: 'auticon', // the audience set for the auth0 app
    clientId: 'aTMdTp47FlBU4JA9WIWYzOqPazLymZ4K', // the client id generated for the auth0 app
    callbackURL: 'http://localhost:4200', // the base url of the running ionic application. 
  }
};



