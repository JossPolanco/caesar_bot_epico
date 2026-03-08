const { Client, LocalAuth, MessageMedia } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const axios = require('axios');

const client = new Client({
    authStrategy: new LocalAuth()
});

const FLASK_API = 'http://localhost:3000';

const loggedInUsers = new Set();

client.on('qr', (qr) => {
    qrcode.generate(qr, { small: true });
});

client.on('ready', () => {
    console.log('Client is ready!');
});

async function encryptMessage(phrase, shift) {
    try {
        const response = await axios.post(`${FLASK_API}/encrypt`, {
            phrase,
            shift: parseInt(shift)
        });
        return response.data.encrypted;
    } catch (error) {
        console.error('Error encrypting:', error);
        throw error;
    }
}

async function decryptMessage(phrase, shift) {
    try {
        const response = await axios.post(`${FLASK_API}/decrypt`, {
            phrase,
            shift: parseInt(shift)
        });
        return response.data.decrypted;
    } catch (error) {
        console.error('Error decrypting:', error);
        throw error;
    }
}

async function registerUser(phoneNumber, password) {
    try {
        const response = await axios.post(`${FLASK_API}/register`, {
            phoneNumber,
            password
        });
        return response.data.status;
    } catch (error) {
        console.error('Error registering:', error);
        throw error;
    }
}


async function login(phoneNumber, password) {
    try {
        const response = await axios.post(`${FLASK_API}/login`, {
            phoneNumber,
            password
        });
        return response.data.status;
    } catch (error) {
        console.error('Error login:', error);
        throw error;
    }
}

client.on("message", async (message) => {
    if (message.fromMe) return;
    const messageBody = message.body.trim();
    const contact = await message.getContact();
    const phoneNumber = contact.number;

    const cipherMatch = messageBody.match(/^!cypher\s+(.+?)\s+(\d+)\s*$/i);
    const decipherMatch = messageBody.match(/^!decypher\s+(.+?)\s+(\d+)\s*$/i);
    const registerMatch = messageBody.match(/^!register\s+(\S+)\s*$/i);
    const loginMatch = messageBody.match(/^!login\s+(\S+)\s*$/i);
    const logoutMatch = messageBody.match(/^!logout\s*$/i);

    if (registerMatch) {
        try {
            const password = registerMatch[1];
            const status = await registerUser(phoneNumber, password);
            if (status != 'ok') {
                await message.reply(`Error: ${status}`);
            }
            await message.reply(`Status: ${response}`);
        } catch (error) {
            console.error('Error registering user:', error);
        }
    }
    else if (loginMatch) {
        try {
            const password = loginMatch[1];
            const status = await login(phoneNumber, password);
            if (status === 'ok') {
                loggedInUsers.add(phoneNumber);
                await message.reply(`Status: ${status}`);
            } else {
                await message.reply(`Status: ${status}`);
            }

        } catch (error) {
            console.error('Error loging user:', error);
        }
    }

    if (!loggedInUsers.has(phoneNumber)) {
        if (cipherMatch || decipherMatch || logoutMatch || messageBody.toLowerCase() === 'ping' || messageBody.toLowerCase() === 'que') {
            await message.reply('You must login first. Use: !login <password>');
        }
        return;
    }

    if (logoutMatch) {
        loggedInUsers.delete(phoneNumber);
        await message.reply('Logout successfully');
    } else if (messageBody.toLowerCase() === 'ping') {
        await message.reply('pong');
    }
    else if (cipherMatch) {
        try {
            const word = cipherMatch[1];
            const shift = cipherMatch[2];

            const encrypted = await encryptMessage(word, shift);
            await message.reply(`Encrypted: ${encrypted}`);
        } catch (error) {
            await message.reply('Error encrypting the message');
        }
    } else if (decipherMatch) {
        try {
            const word = decipherMatch[1];
            const shift = decipherMatch[2];

            const decrypted = await decryptMessage(word, shift);
            await message.reply(`Decrypted: ${decrypted}`);
        } catch (error) {
            await message.reply('Error decrypting the message');
        }
    } else if (message.body.toLowerCase() === 'que') {
        const url = "https://images7.memedroid.com/images/UPLOADED574/625f4dd6290b4.jpeg";
        try {
            const media = await MessageMedia.fromUrl(url);
            await client.sendMessage(message.from, media, {
                sendMediaAsSticker: true,
                stickerAuthor: "yo",
                stickerName: "sticker"
            });
        } catch (error) {
            console.error('Error sending sticker:', error);
        }
    }
});

client.initialize();