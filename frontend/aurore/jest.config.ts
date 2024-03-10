/// <reference types="node" />

module.exports = {
    preset: 'jest-preset-angular',
    setupFilesAfterEnv: ['<rootDir>/setup-jest.ts'],
    globalSetup: 'jest-preset-angular/global-setup',
    testPathIgnorePatterns: [
        '<rootDir>/src/test.ts',
        '<rootDir>/node_modules/',
    ],
    collectCoverageFrom: [
        'src/**/*.ts',
        '!src/test.ts',
        '!**/node_modules/**',
        '!**/vendor/**',
    ],
    roots: ['<rootDir>'],
    modulePaths: ['<rootDir>'],
    coverageDirectory: './coverage/',
    moduleDirectories: ['node_modules', 'src'],
    coverageReporters: ['text', 'html', 'coverage'],
};