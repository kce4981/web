"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const inputBox_html_1 = __importDefault(require("../html/inputBox.html"));
var inbox = document.createElement(inputBox_html_1.default);
document.getElementsByClassName('InputBox')[0] = inbox;
