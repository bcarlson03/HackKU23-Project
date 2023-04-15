
def main(output):  # output will be a list
    final_output = ''
    for result in output:
        for line in result.split('\n'):
            if line.strip()[:13] == 'transcript: "':
                final_output += (line.strip()[13:-1])
                if final_output[-1] not in ['.', '!', '?']:
                    final_output += '. '
    return final_output
