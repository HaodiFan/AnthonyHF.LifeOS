import FlowArt, { FlowSection } from '@/components/ui/story-scroll';
import type { LucideIcon } from 'lucide-react';
import {
  Activity,
  ArrowUpRight,
  BookOpen,
  Brain,
  Code2,
  Cpu,
  Database,
  Dumbbell,
  FileText,
  Github,
  Layers,
  Link,
  Network,
  Route,
  ShieldCheck,
  Sparkles,
  Terminal,
  UserRound,
} from 'lucide-react';

type RouteItem = {
  eyebrow: string;
  title: string;
  copy: string;
  href: string;
  icon: LucideIcon;
};

const asset = (path: string) => `${import.meta.env.BASE_URL}${path.replace(/^\//, '')}`;

const repo = 'https://github.com/HaodiFan/AnthonyHF.Skill';
const afWiki = 'https://haodifan.github.io/AF-wiki/';

const topRoutes: RouteItem[] = [
  {
    eyebrow: 'Human',
    title: 'README.md',
    copy: '公开身份、能力主线和使用说明。',
    href: `${repo}/blob/main/README.md`,
    icon: FileText,
  },
  {
    eyebrow: 'Agent',
    title: 'SKILL.md',
    copy: 'AI 进入 Anthony 上下文前先读的协议。',
    href: `${repo}/blob/main/SKILL.md`,
    icon: Terminal,
  },
  {
    eyebrow: 'Machine',
    title: 'matrix.yml',
    copy: '给工具和 agent 读取的结构化索引。',
    href: `${repo}/blob/main/matrix.yml`,
    icon: Database,
  },
  {
    eyebrow: 'Memory',
    title: 'AF-wiki',
    copy: '健身、知识、工作和项目的长期记忆。',
    href: afWiki,
    icon: Brain,
  },
];

const layers = [
  {
    number: '01',
    title: 'Identity',
    path: 'identity/',
    copy: '问心报告、PSP、公开身份材料。回答“Anthony 是谁”。',
    accent: 'bg-[#75d7ff]',
    icon: UserRound,
  },
  {
    number: '02',
    title: 'Skills',
    path: 'skills/',
    copy: 'Engineering Everything、自我更新，以及未来的产品/组织能力。',
    accent: 'bg-[#96f2e5]',
    icon: Code2,
  },
  {
    number: '03',
    title: 'Memory',
    path: 'memory/af-wiki/',
    copy: 'LeadFlow second brain。持续维护 fitness、knowledge、work areas。',
    accent: 'bg-[#f0c15b]',
    icon: Network,
  },
  {
    number: '04',
    title: 'Security',
    path: 'security/',
    copy: '公开边界。原始会议、客户细节、私有文档和密钥不进入公开仓库。',
    accent: 'bg-[#ff765f]',
    icon: ShieldCheck,
  },
];

const knowledgeTopics = [
  'Agent Memory',
  'Agent Runtime',
  'Function Calling',
  'LLM Safety',
  'Self-Evolving AI',
  'AI4Science',
  'Data Management',
  'Workflow Runtime',
];

const fitnessLoop = [
  'Profile',
  'Goals',
  'Current Plan',
  'Decision Rules',
  'Check-ins',
  'Week Reviews',
  'Nutrition',
  'Structured DB',
];

const networkRoutes: RouteItem[] = [
  {
    eyebrow: 'Profile',
    title: 'GitHub Home',
    copy: '公开主页和项目门面。',
    href: 'https://github.com/HaodiFan',
    icon: Github,
  },
  {
    eyebrow: 'Second Brain',
    title: 'AF-wiki Map',
    copy: '健身记忆、知识图谱、source boundary 和 area 导航。',
    href: afWiki,
    icon: Brain,
  },
  {
    eyebrow: 'Avatar Skill',
    title: 'AnthonyHF.Skill',
    copy: '当前页面。人读 profile，AI 读 protocol。',
    href: 'https://haodifan.github.io/AnthonyHF.Skill/',
    icon: Sparkles,
  },
  {
    eyebrow: 'App',
    title: 'ChatGPT Next Web',
    copy: '应用层 AI chat deployment。',
    href: 'https://chat-gpt-next-web-haodifan.vercel.app',
    icon: Link,
  },
];

function ExternalAnchor({
  href,
  children,
  className,
  ariaLabel,
}: {
  href: string;
  children: React.ReactNode;
  className?: string;
  ariaLabel?: string;
}) {
  return (
    <a
      href={href}
      aria-label={ariaLabel}
      target="_blank"
      rel="noreferrer"
      className={className}
    >
      {children}
    </a>
  );
}

function RouteCard({ item }: { item: RouteItem }) {
  const Icon = item.icon;

  return (
    <ExternalAnchor
      href={item.href}
      className="group flex min-h-[128px] flex-col justify-between rounded-lg border border-white/15 bg-white/[0.06] p-4 transition hover:-translate-y-0.5 hover:border-white/35 hover:bg-white/[0.12] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#96f2e5]"
    >
      <div className="flex items-center justify-between gap-3">
        <span className="font-mono text-[11px] uppercase text-white/60">{item.eyebrow}</span>
        <Icon aria-hidden="true" className="h-4 w-4 text-[#96f2e5]" />
      </div>
      <div>
        <strong className="block text-lg font-semibold leading-tight text-white">{item.title}</strong>
        <span className="mt-2 block text-sm leading-relaxed text-white/62">{item.copy}</span>
      </div>
    </ExternalAnchor>
  );
}

function LogoTile({ src, alt }: { src: string; alt: string }) {
  return (
    <div className="flex h-16 items-center justify-center rounded-lg border border-white/12 bg-white/[0.05] px-4">
      <img src={src} alt={alt} className="max-h-9 w-auto object-contain opacity-90" />
    </div>
  );
}

function App() {
  return (
    <>
      <header className="fixed left-0 right-0 top-0 z-50 flex min-h-14 items-center justify-between gap-4 border-b border-white/10 bg-[#06111d]/70 px-4 text-white backdrop-blur-xl md:px-8">
        <ExternalAnchor href="https://haodifan.github.io/AnthonyHF.Skill/" className="flex items-center gap-3">
          <span className="grid h-8 w-8 place-items-center rounded-lg border border-[#96f2e5]/50 bg-[#96f2e5]/10 font-mono text-xs font-bold text-[#96f2e5]">
            AF
          </span>
          <span className="hidden text-sm font-semibold sm:block">AnthonyHF.Skill</span>
        </ExternalAnchor>
        <nav aria-label="Public route links" className="flex items-center gap-2">
          <ExternalAnchor
            href={repo}
            className="inline-flex h-9 items-center gap-2 rounded-lg border border-white/14 px-3 text-xs font-semibold text-white/78 transition hover:bg-white/10 hover:text-white"
          >
            <Github aria-hidden="true" className="h-4 w-4" />
            <span className="hidden sm:inline">Repo</span>
          </ExternalAnchor>
          <ExternalAnchor
            href={afWiki}
            className="inline-flex h-9 items-center gap-2 rounded-lg border border-white/14 px-3 text-xs font-semibold text-white/78 transition hover:bg-white/10 hover:text-white"
          >
            <Brain aria-hidden="true" className="h-4 w-4" />
            <span className="hidden sm:inline">AF-wiki</span>
          </ExternalAnchor>
        </nav>
      </header>

      <FlowArt aria-label="AnthonyHF.Skill public story scroll">
        <FlowSection
          aria-label="AnthonyHF.Skill hero"
          style={{
            background:
              'radial-gradient(circle at 75% 20%, rgba(117, 215, 255, 0.28), transparent 34%), linear-gradient(135deg, #06111d 0%, #0d263c 58%, #dbeef8 100%)',
            color: '#fff',
          }}
        >
          <div className="mt-12 flex items-center justify-between gap-4 text-xs text-white/68">
            <span className="font-mono uppercase">Public avatar interface</span>
            <span className="font-mono uppercase">Human-readable / Agent-readable</span>
          </div>

          <div className="grid min-h-0 flex-1 items-center gap-6 lg:grid-cols-[0.95fr_1.05fr]">
            <div className="max-w-3xl">
              <p className="mb-4 inline-flex rounded-lg border border-[#96f2e5]/35 bg-[#96f2e5]/10 px-3 py-2 font-mono text-xs text-[#b9fff6]">
                Identity + Skills + AF-wiki + Security
              </p>
              <h1 className="text-balance text-[clamp(3rem,9vw,8.5rem)] font-extrabold leading-[0.92]">
                AnthonyHF.
                <br />
                Skill
              </h1>
              <p className="mt-5 max-w-[58ch] text-[clamp(1rem,2vw,1.45rem)] leading-relaxed text-white/78">
                一个给人和 AI 共用的公开入口：人看见 Anthony Fan 的能力结构，AI 读到协作协议、长期记忆和公开边界。
              </p>
              <div className="mt-6 flex flex-wrap gap-3">
                <ExternalAnchor
                  href={repo}
                  className="inline-flex h-11 items-center gap-2 rounded-lg bg-[#96f2e5] px-4 text-sm font-bold text-[#06111d] transition hover:bg-white"
                >
                  GitHub Repo
                  <ArrowUpRight aria-hidden="true" className="h-4 w-4" />
                </ExternalAnchor>
                <ExternalAnchor
                  href={`${repo}/blob/main/SKILL.md`}
                  className="inline-flex h-11 items-center gap-2 rounded-lg border border-white/18 bg-white/8 px-4 text-sm font-bold text-white transition hover:bg-white/14"
                >
                  Agent Protocol
                  <ArrowUpRight aria-hidden="true" className="h-4 w-4" />
                </ExternalAnchor>
              </div>
            </div>

            <div className="relative mx-auto w-full max-w-[820px]">
              <div className="absolute -inset-6 rounded-lg bg-white/10 blur-2xl" aria-hidden="true" />
              <img
                src={asset('assets/personal/anthonyhf-readme-cover.png')}
                alt="AnthonyHF.Skill digital avatar interface map"
                className="relative aspect-[1672/941] w-full rounded-lg border border-white/20 bg-[#eef7fb] object-contain shadow-[0_28px_90px_rgba(0,0,0,0.36)]"
              />
            </div>
          </div>

          <div className="grid gap-2 text-xs text-white/62 sm:grid-cols-3">
            <div className="rounded-lg border border-white/12 bg-white/[0.06] p-3">
              <span className="font-mono text-[#96f2e5]">Owner</span>
              <strong className="mt-1 block text-base text-white">Anthony Fan</strong>
            </div>
            <div className="rounded-lg border border-white/12 bg-white/[0.06] p-3">
              <span className="font-mono text-[#96f2e5]">Role</span>
              <strong className="mt-1 block text-base text-white">Public identity router</strong>
            </div>
            <div className="rounded-lg border border-white/12 bg-white/[0.06] p-3">
              <span className="font-mono text-[#96f2e5]">Runtime</span>
              <strong className="mt-1 block text-base text-white">React + GSAP ScrollTrigger</strong>
            </div>
          </div>
        </FlowSection>

        <FlowSection
          aria-label="Identity layer"
          style={{
            background:
              'linear-gradient(135deg, #f7fbff 0%, #e8f4fb 48%, #fff6e6 100%)',
            color: '#071420',
          }}
        >
          <div className="mt-12 flex items-center justify-between text-xs text-[#2f6d80]">
            <span className="font-mono uppercase">02 / Identity</span>
            <span className="font-mono uppercase">Public profile, not private evidence</span>
          </div>

          <div className="grid flex-1 items-center gap-6 lg:grid-cols-[0.9fr_1.1fr]">
            <div className="grid gap-3 sm:grid-cols-[minmax(0,0.72fr)_minmax(180px,0.5fr)]">
              <div className="relative overflow-hidden rounded-lg border border-[#071420]/12 bg-white shadow-[0_24px_70px_rgba(7,20,32,0.18)]">
                <img
                  src={asset('assets/personal/selfie.jpg')}
                  alt="Anthony Fan portrait"
                  className="aspect-[4/5] h-full max-h-[430px] w-full object-cover"
                />
                <div className="absolute bottom-4 left-4 rounded-lg border border-[#071420]/12 bg-white/88 px-4 py-3 text-sm shadow-lg backdrop-blur">
                  <span className="font-mono text-xs text-[#2f6d80]">Public identity</span>
                  <strong className="block text-lg">29 岁 · 20 年码龄</strong>
                </div>
              </div>

              <div className="grid gap-3">
                <div className="rounded-lg border border-[#071420]/12 bg-white/76 p-4 shadow-[0_18px_55px_rgba(7,20,32,0.1)]">
                  <div className="mb-5 flex items-center justify-between gap-3">
                    <span className="grid h-10 w-10 place-items-center rounded-lg bg-[#12354a] text-white">
                      <Route aria-hidden="true" className="h-5 w-5" />
                    </span>
                    <span className="font-mono text-xs text-[#2f6d80]">identity/</span>
                  </div>
                  <strong className="block text-xl leading-tight">身份不是素材堆</strong>
                  <p className="mt-3 text-sm leading-relaxed text-[#52687a]">
                    公开叙事、PSP、问心报告和安全边界分层读取。
                  </p>
                </div>
                <div className="rounded-lg border border-[#071420]/12 bg-[#071420] p-4 text-white shadow-[0_18px_55px_rgba(7,20,32,0.14)]">
                  <span className="font-mono text-xs text-[#96f2e5]">read order</span>
                  <div className="mt-3 grid gap-2 font-mono text-xs text-white/72">
                    <span>README.md</span>
                    <span>SKILL.md</span>
                    <span>identity/psp</span>
                    <span>security/README</span>
                  </div>
                </div>
              </div>
            </div>

            <div>
              <p className="mb-4 font-mono text-xs uppercase text-[#2f6d80]">
                Continuous founder / engineer / AI delivery
              </p>
              <h2 className="text-balance text-[clamp(2.35rem,5.6vw,5.1rem)] font-extrabold leading-[0.95]">
                不是简历页。
                <br />
                是一个可读取的工作系统。
              </h2>
              <p className="mt-5 max-w-[58ch] text-[clamp(1rem,1.8vw,1.28rem)] leading-relaxed text-[#385165]">
                AnthonyHF.Skill 把公开身份、工程判断、长期记忆和安全边界放进同一个结构里。它的目标不是包装个人品牌，而是让人和 AI 更准确地进入上下文。
              </p>
            </div>
          </div>

          <div className="hidden gap-3 md:grid md:grid-cols-3">
            {[
              ['底层穿透', '从软硬件到企业 AI，把复杂系统拆到底层再重建。'],
              ['业务闭环', '技术最后要落到客户、产品、交付和现金流。'],
              ['长期复利', '持续学习，把多年积累变成下一次构建的资本。'],
            ].map(([title, copy]) => (
              <div key={title} className="rounded-lg border border-[#071420]/12 bg-white/70 p-4">
                <strong className="block text-lg">{title}</strong>
                <span className="mt-2 block text-sm leading-relaxed text-[#52687a]">{copy}</span>
              </div>
            ))}
          </div>
        </FlowSection>

        <FlowSection
          aria-label="Skill matrix"
          style={{
            background:
              'radial-gradient(circle at 18% 18%, rgba(150, 242, 229, 0.18), transparent 30%), linear-gradient(135deg, #090c0b 0%, #121713 56%, #20352c 100%)',
            color: '#fff',
          }}
        >
          <div className="mt-12 flex items-center justify-between text-xs text-white/56">
            <span className="font-mono uppercase">03 / Skill Matrix</span>
            <span className="font-mono uppercase">shadcn path: components/ui</span>
          </div>

          <div className="grid flex-1 items-center gap-6 xl:grid-cols-[0.86fr_1.14fr]">
            <div>
              <p className="mb-4 font-mono text-xs uppercase text-[#96f2e5]">Protocol as interface</p>
              <h2 className="text-balance text-[clamp(2.3rem,5vw,4.35rem)] font-extrabold leading-[0.95]">
                AI 进入这里后，先判断该读哪一层。
              </h2>
              <p className="mt-5 max-w-[58ch] text-[clamp(1rem,1.7vw,1.22rem)] leading-relaxed text-white/66">
                这个仓库不是把所有东西都公开，而是把公开层、身份层、能力层、记忆层和安全层分清楚。
              </p>
            </div>

            <div className="grid gap-3 md:grid-cols-2">
              {layers.map((layer) => {
                const Icon = layer.icon;

                return (
                  <ExternalAnchor
                    key={layer.title}
                    href={`${repo}/tree/main/${layer.path}`}
                    className="group min-h-[154px] rounded-lg border border-white/12 bg-white/[0.055] p-4 transition hover:-translate-y-0.5 hover:border-white/32 hover:bg-white/[0.1] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#96f2e5]"
                  >
                    <div className="mb-5 flex items-center justify-between gap-3">
                      <span className="font-mono text-xs text-white/52">{layer.number}</span>
                      <span className={`h-2.5 w-10 rounded-full ${layer.accent}`} />
                    </div>
                    <div className="flex items-start gap-3">
                      <Icon aria-hidden="true" className="mt-1 h-5 w-5 text-[#96f2e5]" />
                      <div>
                        <strong className="block text-xl">{layer.title}</strong>
                        <span className="mt-1 block font-mono text-xs text-white/42">{layer.path}</span>
                        <p className="mt-3 text-sm leading-relaxed text-white/62">{layer.copy}</p>
                      </div>
                    </div>
                  </ExternalAnchor>
                );
              })}
            </div>
          </div>

          <div className="grid grid-cols-2 gap-2 sm:grid-cols-5">
            <LogoTile src={asset('assets/logos/nvidia-logo-clean.png')} alt="NVIDIA logo" />
            <LogoTile src={asset('assets/logos/grainedai-logo-clean.png')} alt="GrainedAI logo" />
            <LogoTile src={asset('assets/logos/metainflow-logo.png')} alt="MetaInFlow logo" />
            <LogoTile src={asset('assets/logos/snapanthony-logo.png')} alt="SnapAnthony logo" />
            <LogoTile src={asset('assets/logos/shellprobe-logo.jpg')} alt="ShellProbe logo" />
          </div>
        </FlowSection>

        <FlowSection
          aria-label="AF-wiki knowledge and fitness map"
          style={{
            background:
              'linear-gradient(135deg, #eaf8f4 0%, #f8fbff 48%, #f9f3e1 100%)',
            color: '#08201c',
          }}
        >
          <div className="mt-12 flex items-center justify-between text-xs text-[#256357]">
            <span className="font-mono uppercase">04 / AF-wiki</span>
            <span className="font-mono uppercase">Fitness + Knowledge as operating memory</span>
          </div>

          <div className="grid flex-1 items-center gap-6 xl:grid-cols-[0.9fr_1.1fr]">
            <div>
              <p className="mb-4 inline-flex rounded-lg border border-[#0b6b58]/20 bg-white/80 px-3 py-2 font-mono text-xs uppercase text-[#256357]">
                LeadFlow second brain
              </p>
              <h2 className="text-balance text-[clamp(2.3rem,5vw,4.3rem)] font-extrabold leading-[0.95]">
                健身和知识不是笔记堆。
                <br />
                是可路由的记忆系统。
              </h2>
              <p className="mt-5 max-w-[62ch] text-[clamp(1rem,1.65vw,1.2rem)] leading-relaxed text-[#3f5d57]">
                AF-wiki 现在按动态 area 组织。Fitness 维护计划、记录、营养、周复盘和结构化数据；Knowledge 维护 agent systems map、source manifests、topics 和 retained notes。
              </p>
            </div>

            <div className="grid gap-3 md:grid-cols-2">
              <div className="rounded-lg border border-[#08201c]/12 bg-white/72 p-4">
                <div className="mb-4 flex items-center gap-3">
                  <span className="grid h-10 w-10 place-items-center rounded-lg bg-[#0b6b58] text-white">
                    <Dumbbell aria-hidden="true" className="h-5 w-5" />
                  </span>
                  <div>
                    <strong className="block text-xl">Fitness Area</strong>
                    <span className="font-mono text-xs text-[#5d756f]">areas/fitness/</span>
                  </div>
                </div>
                <div className="grid grid-cols-2 gap-2">
                  {fitnessLoop.map((item) => (
                    <span key={item} className="rounded-lg border border-[#08201c]/10 bg-[#f7fbf8] px-3 py-2 text-sm font-semibold text-[#2d514a]">
                      {item}
                    </span>
                  ))}
                </div>
              </div>

              <div className="rounded-lg border border-[#08201c]/12 bg-white/72 p-4">
                <div className="mb-4 flex items-center gap-3">
                  <span className="grid h-10 w-10 place-items-center rounded-lg bg-[#153f6b] text-white">
                    <BookOpen aria-hidden="true" className="h-5 w-5" />
                  </span>
                  <div>
                    <strong className="block text-xl">Knowledge Area</strong>
                    <span className="font-mono text-xs text-[#5d756f]">areas/knowledge/</span>
                  </div>
                </div>
                <div className="grid grid-cols-2 gap-2">
                  {knowledgeTopics.map((item) => (
                    <span key={item} className="rounded-lg border border-[#08201c]/10 bg-[#f7fbff] px-3 py-2 text-sm font-semibold text-[#314f6c]">
                      {item}
                    </span>
                  ))}
                </div>
              </div>
            </div>
          </div>

          <div className="hidden grid-cols-4 gap-3 2xl:grid">
            {[
              ['START-HERE', '第一次进入 AF-wiki 的导览。'],
              ['areas/index', '当前 area registry 和 skill routing。'],
              ['source manifests', '只保存 provenance，不保存原文。'],
              ['public boundary', 'Git 仓库只放抽象、索引和萃取。'],
            ].map(([title, copy]) => (
              <div key={title} className="rounded-lg border border-[#08201c]/10 bg-white/64 p-4">
                <span className="font-mono text-xs text-[#256357]">{title}</span>
                <p className="mt-2 text-sm leading-relaxed text-[#4c625d]">{copy}</p>
              </div>
            ))}
          </div>
        </FlowSection>

        <FlowSection
          aria-label="Deployment network"
          style={{
            background:
              'radial-gradient(circle at 70% 18%, rgba(255, 180, 84, 0.2), transparent 26%), linear-gradient(135deg, #050505 0%, #12100b 58%, #1c2524 100%)',
            color: '#fff',
          }}
        >
          <div className="mt-12 flex items-center justify-between text-xs text-white/56">
            <span className="font-mono uppercase">05 / Deployment Network</span>
            <span className="font-mono uppercase">Pages, profile, apps</span>
          </div>

          <div className="grid flex-1 items-center gap-6 xl:grid-cols-[0.82fr_1.18fr]">
            <div>
              <p className="mb-4 font-mono text-xs uppercase text-[#ffcf83]">Linked public surfaces</p>
              <h2 className="text-balance text-[clamp(2.3rem,5.2vw,4.7rem)] font-extrabold leading-[0.95]">
                这不是孤立页面。
                <br />
                它是公开系统入口。
              </h2>
              <p className="mt-5 max-w-[58ch] text-[clamp(1rem,1.7vw,1.22rem)] leading-relaxed text-white/66">
                GitHub Profile 负责门面，AF-wiki 负责长期记忆，AnthonyHF.Skill 负责分身协议，应用部署负责真实可用的工具入口。
              </p>
            </div>

            <div className="grid gap-3 md:grid-cols-2">
              {networkRoutes.map((item) => (
                <RouteCard key={item.title} item={item} />
              ))}
            </div>
          </div>

          <div className="hidden gap-3 2xl:grid 2xl:grid-cols-[1fr_1fr_1.2fr]">
            <div className="rounded-lg border border-white/12 bg-white/[0.055] p-3">
              <img
                src={asset('assets/products/snapanthony-product.png')}
                alt="SnapAnthony product preview"
                className="h-28 w-full rounded-lg object-contain"
              />
            </div>
            <div className="rounded-lg border border-white/12 bg-white/[0.055] p-3">
              <img
                src={asset('assets/products/shellprobe-product.jpg')}
                alt="ShellProbe product preview"
                className="h-28 w-full rounded-lg object-cover"
              />
            </div>
            <div className="rounded-lg border border-white/12 bg-white/[0.055] p-4">
              <div className="flex items-start gap-3">
                <Activity aria-hidden="true" className="mt-1 h-5 w-5 text-[#ffcf83]" />
                <div>
                  <strong className="block text-lg">React on GitHub Pages</strong>
                  <p className="mt-2 text-sm leading-relaxed text-white/62">
                    Vite build 输出静态文件；`base` 已设为 `/AnthonyHF.Skill/`，可以部署到 `gh-pages` 分支。
                  </p>
                </div>
              </div>
            </div>
          </div>
        </FlowSection>
      </FlowArt>
    </>
  );
}

export default App;
