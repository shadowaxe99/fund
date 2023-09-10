const Campaign = require('./campaign');
const EmailSender = require('./emailSender');
const ResponseHandler = require('./responseHandler');
const Analytics = require('./analytics');
const Integration = require('./integration');
const Security = require('./security');
const Scalability = require('./scalability');

class App {
  constructor() {
    this.campaign = new Campaign();
    this.emailSender = new EmailSender(this.campaign);
    this.responseHandler = new ResponseHandler();
    this.analytics = new Analytics(this.campaign);
    this.integration = new Integration();
    this.security = new Security();
    this.scalability = new Scalability();
  }

  run() {
    this.campaign.createCampaign();
    this.emailSender.sendEmail();
    this.responseHandler.analyzeResponse();
    this.analytics.track_opens();
    this.integration.integrate();
    this.security.encrypt();
    this.scalability.scaleHorizontally();
  }
}

module.exports = App;