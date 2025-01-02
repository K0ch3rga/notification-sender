import * as fs from 'fs';
import * as path from 'path';

const tokenFilePath = path.join(__dirname, 'token.txt');
const token = fs.existsSync(tokenFilePath)
    ? fs.readFileSync(tokenFilePath, 'utf-8').trim()
    : '';

export const telegramConfig = {
    botToken: process.env.TELEGRAM_BOT_TOKEN || token,
};
