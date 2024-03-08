import { defineConfig } from "cypress";
import coverageTask from "@cypress/code-coverage/task";

import { addCucumberPreprocessorPlugin } from "@badeball/cypress-cucumber-preprocessor";
import createBundler from "@bahmutov/cypress-esbuild-preprocessor";
import { createEsbuildPlugin } from "@badeball/cypress-cucumber-preprocessor/esbuild";

export default defineConfig({
  video: false,
  viewportWidth: 1280,
  viewportHeight: 720,
  defaultCommandTimeout: 5000,
  execTimeout: 60000,

  retries: {
    runMode: 1,
    openMode: 0,
  },

  chromeWebSecurity: false,

  env: {
    codeCoverage: {
      exclude: ["cypress/**/*.*", "coverage/**/*.*"],
    },
  },

  e2e: {
    async setupNodeEvents(
      on: Cypress.PluginEvents,
      config: Cypress.PluginConfigOptions
    ): Promise<Cypress.PluginConfigOptions> {
      await addCucumberPreprocessorPlugin(on, config);

      on(
        "file:preprocessor",
        createBundler({
          plugins: [createEsbuildPlugin(config)]
        })
      );

      coverageTask(on, config);

      return config;
    },
    baseUrl: "http://localhost:4200",
    specPattern: "cypress/e2e/features/*.feature",
  },

  component: {
    devServer: {
      framework: "angular",
      bundler: "webpack",
    },
    specPattern: "**/*.cy.ts",
  },
});
