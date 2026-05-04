import re

with open("index.html", "r") as f:
    content = f.read()

# Update 公司初心 (lines ~326-333)
old_company_goal = """                        <!-- Bottom Bar -->
                        <div class="w-full relative mt-auto">
                            <!-- Extending the background to the left outside the container to cover the padding area -->
                            <div class="absolute -left-6 sm:-left-8 top-0 bottom-0 w-8 bg-primary rounded-l-lg z-0"></div>
                            
                            <div class="bg-primary text-white p-5 rounded-r-lg rounded-bl-lg flex flex-col sm:flex-row justify-between items-start sm:items-center shadow-[0_10px_30px_rgba(210,0,0,0.2)] relative z-10 w-full sm:-ml-2">
                                <div class="font-serif font-bold text-2xl mb-2 sm:mb-0 whitespace-nowrap">公司初心</div>
                                <div class="font-sans text-xs sm:text-sm tracking-[2px] text-white/90 text-right w-full">创新、拼搏、担当、感恩、诚信</div>
                            </div>
                        </div>"""

new_company_goal = """                        <!-- Bottom Bar -->
                        <div class="w-full relative mt-auto flex items-stretch pt-4">
                            <!-- Thin red line -->
                            <div class="w-1.5 bg-[#cc0000] flex-shrink-0"></div>
                            <!-- Main red box -->
                            <div class="ml-1.5 sm:ml-2 flex-grow bg-[#cc0000] rounded-lg sm:rounded-xl p-5 sm:p-8 flex flex-col justify-between min-h-[140px] shadow-[0_10px_30px_rgba(204,0,0,0.3)]">
                                <div class="font-serif text-3xl sm:text-4xl text-white font-bold tracking-widest text-left">公司初心</div>
                                <div class="font-sans text-sm sm:text-base tracking-[0.2em] text-white/90 text-right mt-12 sm:mt-16">创新、拼搏、担当、感恩、诚信</div>
                            </div>
                        </div>"""

# Ensure old_company_goal matches safely
start_idx = content.find("<!-- Bottom Bar -->")
if start_idx != -1:
    end_idx = content.find("</div>", content.find("</div>", content.find("</div>", content.find("公司初心")))) + 6
    # This might be tricky, let's just do a replace
    content = content.replace(old_company_goal, new_company_goal)

# Update Media section grid
# Find: <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 bg-[#0a0a0a] border border-[#222] fade-up">
old_media_grid = '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 bg-[#0a0a0a] border border-[#222] fade-up">'
new_media_grid = '<div class="grid grid-cols-2 lg:grid-cols-4 bg-[#0a0a0a] border border-[#222] fade-up">'
content = content.replace(old_media_grid, new_media_grid)

# Also fix the borders for Media grid in 2-column layout to avoid missing borders
# we'll update the padding and text size if needed to fit 2 cols on mobile
content = re.sub(r'py-16 px-6 text-center focus?', r'py-10 px-3 sm:py-16 sm:px-6 text-center', content) # reduce padding on mobile
# reduce font sizes slightly so it doesn't break in 2 col
content = content.replace('text-5xl md:text-6xl text-primary', 'text-4xl sm:text-5xl md:text-6xl text-primary')
content = content.replace('text-6xl md:text-7xl text-primary', 'text-5xl sm:text-6xl md:text-7xl text-primary')
content = content.replace('text-6xl md:text-7xl text-white font-serif font-black', 'text-5xl sm:text-6xl md:text-7xl text-white font-serif font-black') # the red box 2
content = content.replace('text-lg md:text-xl text-white', 'text-sm sm:text-lg md:text-xl text-white')
content = content.replace('text-xs md:text-sm text-gray-400', 'text-[10px] sm:text-xs md:text-sm text-gray-400')


with open("index.html", "w") as f:
    f.write(content)
print("Updated successfully")

